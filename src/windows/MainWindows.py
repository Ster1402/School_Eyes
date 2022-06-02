
import hashlib
import json
import os
from pprint import pprint
import re
from time import ctime, sleep

from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation, QThread
from PyQt5.QtWidgets import (
    QMainWindow, 
    QTableWidgetItem, 
    QMessageBox, 
    QPushButton, 
    QDialog,
    QFileDialog)

import cv2
from src.windows.DialogStudent import DiaglogStudent
from src.windows.DialogRequestParams import DiaglogRequestParams

from src.windows_ui.UI_MainWindows import Ui_MainWindow

from src.database.db import DB, DisciplineModel, StudentModel
from src.model.Classroom import Classroom
from src.model.Student import Student
from src.utils.Worker import Worker
from src.utils.FaceReconizer import FaceReconizer
from src.utils.ListFormatter import ListFormatter
from src.utils.Request import Request
                        
class MainWindows(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)

        self._translate = QtCore.QCoreApplication.translate

        # Home windows
        self.__adminConnectionVerification()
        self.index()

        # Establishing slots connection
        self.__slots_connection()

    def index(self):
        # If the user is connected, show home widget
        if self.connected:
            self.showHome()
        else:
            self.logout()

    def showHome(self):
        self.activate_menu_button()
        self.stacked_widget.setCurrentWidget(self.page_home)
        self.__initialize_pages_data()

    def printLoginError(self):
        QMessageBox.warning(self,
                            self._translate("LoginError", "Login Error"),
                            self._translate("ErrorMessage", "We could'nt find the corresponding account,\
please make sure that the informations provide are correct."))

    def __adminConnectionVerification(self):
        # Check if an admin is connected
        self.admin_connected = DB.adminConnected()
        # If an admin is connected we have (id, login, password) in admin_connected

        self.connected = self.admin_connected != None

    def login(self):
        # Check login and password
        login = self.username_login.text()
        password = hashlib.md5(bytes(self.password_login.text(), "utf8"))\
                          .hexdigest()

        self.admin_connected = DB.checkIfAdminExist(login, password)

        if not self.admin_connected:
            self.printLoginError()
            self.password_login.clear()
        else:
            DB.connectAdmin(self.admin_connected[0])
            self.changeBtnMenuColor(self.btn_menu_home)
            self.showHome()

    def logout(self):
        DB.disconnectAdmin()
        self.activate_menu_button(False)
        self.password_login.clear()
        self.username_login.clear()
        self.stacked_widget.setCurrentWidget(self.page_login)

    def __slots_connection(self):
        #
        # --> Home button clicked
        #
        self.btn_home_students.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_home_students))
        self.btn_home_camera.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_home_camera))
        self.btn_home_settings.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_home_settings))
        self.btn_home_help.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_home_help))
        #
        # --> Toggle menu clicked
        #
        self.show_menu = True
        self.btn_show_menu.clicked.connect(lambda: self.toggle_menu())
        #
        # --> Menu button clicked
        #
        self.btn_menu_home.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_menu_home))
        self.btn_menu_camera.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_menu_camera))
        self.btn_menu_students.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_menu_students))
        self.btn_menu_settings.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_menu_settings))
        self.btn_menu_help.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_menu_help))
        self.btn_menu_logout.clicked.connect(
            lambda: self.on_btn_home_clicked(self.btn_menu_logout))
        #
        # --> Page Login
        #
        self.confirm_login.clicked.connect(lambda: self.login())
        self.password_login.returnPressed.connect(lambda: self.login())
        #
        # --> Page Student
        #
        self.btn_save_add_student.clicked.connect(lambda: self.threadAddStudent())
        self.btn_refresh_add_student.clicked.connect(lambda: self._refreshAddStudent())
        
        self.btn_student_show_more.clicked.connect(
            lambda: self.showStudentInformations())
        self.student_discipline_comboBox.currentTextChanged.connect(
            lambda discipline: self._updateAxesAddStudent(discipline))
        self.student_discipline_info_comboBox.currentTextChanged.connect(
            lambda discipline: self._updateAxesInfoStudent(discipline))
        self.btn_student_delete.clicked.connect(lambda: self._deleteStudent())
        self.btn_scan_student.clicked.connect(lambda: self.findStudents())

        self.btn_remove_picture.clicked.connect(
            lambda: self.removeStudentSelectedPictures())
        self.btn_select_pictures.clicked.connect(
            lambda: self.chooseStudentPictures())

        #
        # --> Page Settings
        #
        self.btn_update_account.clicked.connect(lambda: self._updateAccount())

        #
        # --> Page Cameras
        #
        self.btn_add_camera.clicked.connect(self._addCamera)
        self.new_camera_url.returnPressed.connect(self._addCamera)
        self.btn_delete_camera.clicked.connect(lambda: self._deleteCamera())
        self.btn_try_cameras.clicked.connect(self._tryCameras)
        self.select_classroom.currentTextChanged.connect(lambda classroom: self._updateCamerasList(classroom))
             
    def __initialize_pages_data(self):

        #
        # --> Classrooms : Camera page
        #
        self.camera_is_running = False
        self.try_camera_thread = QThread()
        
        self.table_camera.clearContents()

        classrooms_names = Classroom.getClassroomsList()
        self.classrooms = [Classroom(name) for name in classrooms_names]
        self.select_classroom.clear()
        self.select_classroom.addItems(classrooms_names)

        self.select_classroom.setCurrentIndex(0)

        classroom_name = self.select_classroom.currentText()
        self._updateCamerasList(classroom_name)

        self.recognition_launched = False

        #
        # --> Page Settings
        #
        if self.connected:
            self.username_settings.setText(self.admin_connected[1])

        #
        # --> Page Student
        #
        self.table_students.clearContents()
        disciplines = DisciplineModel.getDisciplinesName()
        self.student_discipline_info_comboBox.clear()
        self.student_discipline_info_comboBox.addItems(disciplines)
        self.student_axe_info_comboBox.clear()

        self.student_discipline_comboBox.clear()
        self.student_discipline_comboBox.addItems(disciplines)
        self.student_axe_comboBox.clear()

    def activate_btn_menu_color(self, btn: QPushButton, ok: bool):

        if ok:
            if "QPushButton:hover, QPushButton" not in btn.styleSheet():
                btn.setStyleSheet(
                    btn.styleSheet().replace("QPushButton:hover", "QPushButton:hover, QPushButton")
                )
        else:
            btn.setStyleSheet(
                btn.styleSheet().replace("QPushButton:hover, QPushButton", "QPushButton:hover")
            )

    def changeBtnMenuColor(self, sender):
        self.activate_btn_menu_color(self.btn_menu_students, sender.objectName() == "btn_home_students"
                                     or sender.objectName() == "btn_menu_students")
        self.activate_btn_menu_color(self.btn_menu_camera, sender.objectName() == "btn_home_camera"
                                     or sender.objectName() == "btn_menu_camera")
        self.activate_btn_menu_color(self.btn_menu_settings, sender.objectName() == "btn_home_settings"
                                     or sender.objectName() == "btn_menu_settings")
        self.activate_btn_menu_color(self.btn_menu_help, sender.objectName() == "btn_home_help"
                                     or sender.objectName() == "btn_menu_help")
        self.activate_btn_menu_color(
            self.btn_menu_home, sender.objectName() == "btn_menu_home")

        self.activate_btn_menu_color(
            self.btn_menu_logout, sender.objectName() == "btn_menu_logout")

    def on_btn_home_clicked(self, sender):

        self.changeBtnMenuColor(sender)

        if sender.objectName() == "btn_home_students" or sender.objectName() == "btn_menu_students":
            self.stacked_widget.setCurrentWidget(self.page_students)
        elif sender.objectName() == "btn_home_camera" or sender.objectName() == "btn_menu_camera":
            self.stacked_widget.setCurrentWidget(self.page_camera)
        elif sender.objectName() == "btn_home_settings" or sender.objectName() == "btn_menu_settings":
            self.stacked_widget.setCurrentWidget(self.page_settings)
        elif sender.objectName() == "btn_home_help" or sender.objectName() == "btn_menu_help":
            self.stacked_widget.setCurrentWidget(self.page_help)
        elif sender.objectName() == "btn_menu_home":
            self.stacked_widget.setCurrentWidget(self.page_home)
        elif sender.objectName() == "btn_menu_logout":
            self.logout()

    def activate_menu_button(self, ok=True):
        self.btn_menu_home.setEnabled(ok)
        self.btn_menu_students.setEnabled(ok)
        self.btn_menu_camera.setEnabled(ok)
        self.btn_menu_help.setEnabled(True)  # The help button is always active
        self.btn_menu_settings.setEnabled(ok)
        self.btn_menu_logout.setEnabled(True)  # Logout button is always active

    def toggle_menu(self):

        if self.show_menu:

            # Get width
            width = self.menu_left.width()
            maxEntend = 160
            standard_width = 70

            # Set Max Width
            if width == 70:
                widthExtended = maxEntend
            else:
                widthExtended = standard_width

            # Animation
            self.animation = QPropertyAnimation(
                self.menu_left, b'minimumWidth')
            self.animation.setDuration(350)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.BezierSpline)
            self.animation.start()

    #
    # --> Page Student
    #
    def _on_discipline_changed(self):
        discipline = self.student_discipline_comboBox.currentText()

        if discipline == "TCO":
            self.student_level_spinBox.setMaximum(2)
            self.student_level_spinBox.setMinimum(1)
            self.student_axe_comboBox.setEnabled(False)
        else:
            self.student_level_spinBox.setMaximum(5)
            self.student_level_spinBox.setMinimum(3)
            self.student_axe_comboBox.setEnabled(True)

    def _on_discipline_info_changed(self):

        discipline = self.student_discipline_info_comboBox.currentText()

        if discipline == "TCO":
            self.student_level_info_spinBox.setMaximum(2)
            self.student_level_info_spinBox.setMinimum(1)
            self.student_axe_info_comboBox.setEnabled(False)
        else:
            self.student_level_info_spinBox.setMaximum(5)
            self.student_level_info_spinBox.setMinimum(3)
            self.student_axe_info_comboBox.setEnabled(True)

    def chooseStudentPictures(self):
        files = QFileDialog.getOpenFileNames(self,
                                             "Select one or more files to open",
                                             "",
                                             "Images (*.png *.jpeg *.jpg)")
        pictures_path = files[0]
        pictures_path = [path.replace("/", "\\") for path in pictures_path]
        self.drag_and_drop_box.itemsList.update(pictures_path)
        self.drag_and_drop_box.clear()
        self.drag_and_drop_box.addItems(self.drag_and_drop_box.itemsList)

    def removeStudentSelectedPictures(self):

        selectedItems = self.drag_and_drop_box.selectedItems()

        if not selectedItems:
            QMessageBox.information(self, self._translate("Title", "No selection"),
                                    self._translate("WarningMessage", "No picture selected"))
            return

        if QMessageBox.Ok != QMessageBox.warning(self, self._translate("Title", "Delete"),
                                                 self._translate(
                                                     "WarningMessage", "Are you sure that you want to delete these pictures ?"),
                                                 QMessageBox.Ok | QMessageBox.Cancel):
            return

        for selectedItem in selectedItems:

            self.drag_and_drop_box.takeItem(
                self.drag_and_drop_box.row(selectedItem))

            items = [self.drag_and_drop_box.item(
                i) for i in range(self.drag_and_drop_box.count())]
            items = set([item.text() for item in items])
            self.drag_and_drop_box.itemsList = items

    def _addStudent(self):

        name = self.student_name_lineEdit.text()
        # Verification
        if not name:
            self.__empytFieldWarning("Name")
            return

        surname = self.student_surname_lineEdit.text()

        register_number = self.student_register_number_lineEdit.text()
        # Verification
        if not register_number:
            self.__empytFieldWarning("Register Number")
            return

        level = self.student_level_spinBox.value()

        axe = self.student_axe_comboBox.currentText()
        # Verification
        if not axe:
            self.__empytFieldWarning("Axe")
            return

        pictures = self.drag_and_drop_box.itemsList

        student = {
            "name": name + " _ " + surname,
            "register_number": register_number,
            "level": level
        }

        StudentModel.insertStudent(student, axe)

        errors = []
   
        for picture in pictures:

            try:
                StudentModel.addStudentPicture(picture, register_number)
            except ValueError:
                errors.append(f"""- Error trying to add the picture : \nPath : {picture}""")

        if errors:
            raise ValueError(' \n- '.join(errors))

    def threadAddStudent(self):      
        QMessageBox.information(self, self._translate("Title", "Add Student"),
                                self._translate("InfoMessage", "Adding new student... !"))

        self.loader = QMessageBox(self)
        self.loader.setWindowTitle("Processing...")
        self.loader.setText("Process running, please wait...")
        self.loader.exec()

        self.success_message = QMessageBox(self)
        self.success_message.setWindowTitle(self._translate("Title", "Success")) 
        self.success_message.setText(self._translate("InfoMessage", "Student successfully added !"))

        self.btn_save_add_student.setEnabled(False)

        self.add_student_worker = Worker(lambda: self._addStudent())
        self.add_student_thread = QThread()
        
        self.add_student_worker.moveToThread(self.add_student_thread)
        
        self.add_student_thread.started.connect(self.add_student_worker.run)
        self.add_student_thread.started.connect(lambda: self.loader.setEnabled(False))
        self.add_student_worker.finished.connect(self.add_student_thread.quit)
        self.add_student_worker.finished.connect(self.add_student_worker.deleteLater)
        self.add_student_worker.finished.connect(lambda: self.loader.setEnabled(True))
        self.add_student_worker.finished.connect(lambda: self.btn_save_add_student.setEnabled(True))
        self.add_student_worker.finished.connect(lambda: self._refreshAddStudent())
        self.add_student_worker.finished.connect(lambda: self.success_message.exec())
        self.add_student_worker.error_occured.connect(self.printError)

        # Start the thread
        self.add_student_thread.start()
        
        
    def _refreshAddStudent(self):
        self.student_name_lineEdit.clear()
        self.student_surname_lineEdit.clear()
        self.student_register_number_lineEdit.clear()
        self.drag_and_drop_box.clear()
        self.drag_and_drop_box.itemsList.clear()
        
    def __empytFieldWarning(self, field: str) -> None:

        dialog = QMessageBox(self)
        dialog.setWindowTitle(self._translate("Title", "Empty Field"))
        dialog.setText(self._translate("WarningMessage",
                                       f"{field} field can not be empty !"))
        dialog.setIcon(QMessageBox.Warning)

        dialog.exec()

    def findStudents(self):

        # discipline = self.student_discipline_info_comboBox.currentText()

        axe = self.student_axe_info_comboBox.currentText()

        # Verification
        if not axe:
            QMessageBox.warning(self, self._translate("Title", "Empty"),
                                self._translate("InfoMessage", "Axe couldn't be empty."))
            return

        level = self.student_level_info_spinBox.value()

        students = Student.getStudents(axe, level)

        if students:
            self.table_students.clearContents()

            length = len(students)

            for i in range(length):

                name, surname = students[i].get("name").split(" _ ")
                try:
                    self.table_students.removeRow(i)
                except:
                    pass
                self.table_students.insertRow(i)
                self.table_students.setItem(i, 0, QTableWidgetItem(
                    students[i].get("register_number")))
                self.table_students.setItem(i, 1, QTableWidgetItem(name))
                self.table_students.setItem(i, 2, QTableWidgetItem(surname))

        else:
            QMessageBox.information(self, self._translate("Title", "Empty"),
                                    self._translate("InfoMessage", "No student detected."))

    def _deleteStudent(self):
        selectedItems = self.table_students.selectedItems()

        if not selectedItems:
            QMessageBox.warning(self, self._translate("Title", "Empty selection"),
                                self._translate("WarningMessage", "There are no student selected !"))
            return

        register_number = selectedItems[0].text()

        if QMessageBox.Ok != QMessageBox.warning(self, self._translate("Title", "Delete"),
                                                 self._translate(
                                                     "WarningMessage", f"Are you sure that you want to delete this student {register_number} ?"),
                                                 QMessageBox.Ok | QMessageBox.Cancel):
            return

        
        row = self.table_students.row(selectedItems[0])
        StudentModel.removeStudent(register_number)
        self.table_students.removeRow(row)
        
    def _updateAxesAddStudent(self, discipline):
        self.student_axe_comboBox.clear()
        self.student_axe_comboBox.addItems(DisciplineModel.getAxes(discipline))

        if self.student_axe_comboBox.count() > 0:
            self.student_axe_comboBox.setCurrentIndex(0)

        self._on_discipline_changed()

    def _updateAxesInfoStudent(self, discipline):
        self.student_axe_info_comboBox.clear()
        self.student_axe_info_comboBox.addItems(
            DisciplineModel.getAxes(discipline))

        if self.student_axe_info_comboBox.count() > 0:
            self.student_axe_info_comboBox.setCurrentIndex(0)

        self._on_discipline_info_changed()

    def showStudentInformations(self):

        selectedItems = self.table_students.selectedItems()

        if not selectedItems:
            QMessageBox.information(self, self._translate("InfoMessage", "Empty selection"),
                                    self._translate("Message", "There are no student selected !"))
            return

        # Register Number : the value of the first column
        register_number = selectedItems[0].text()

        dialog_student = DiaglogStudent(self, register_number)

        if dialog_student.exec() == QDialog.Accepted:
            self.findStudents()

    #
    # --> Page Cameras
    #
    def _deleteCamera(self):
        
        selectedItems = self.table_camera.selectedItems()

        if not selectedItems:
            QMessageBox.warning(self, self._translate("Title", "Empty selection"),
                                self._translate("WarningMessage", "There are no camera selected !"))
            return

        camera_name = selectedItems[0].text()
        camera_url = selectedItems[1].text()

        if QMessageBox.Ok != QMessageBox.warning(self, self._translate("Title", "Delete"),
                                                 self._translate(
                                                     "WarningMessage", f"Are you sure that you want to delete this camera {camera_name} - {camera_url} ?"),
                                                 QMessageBox.Ok | QMessageBox.Cancel):
            return

        
        row = self.table_camera.row(selectedItems[0])
        classroom: Classroom = selectedItems[0].classroom
        classroom.removeCamera(camera_name)
        self.table_camera.removeRow(row)
    
    def printError(self, error: str):
        QMessageBox.critical(self, self._translate("Title", "Error"),
                                self._translate("ErrorMessage", error))
    
    def _getParamsForVideoReconignition(self):
        
        request = dict()
        
        self.dialogRequestParams = DiaglogRequestParams(self)
        
        if self.dialogRequestParams.exec() != QDialog.Accepted:
            return
        
        request = self.dialogRequestParams.request

        return Request(id=self.admin_connected[0],
                teacher=self.admin_connected[1],
                classroom=request.get("classroom"),
                course="Local Recognition",
                disciplines=request.get("disciplines"),
                level=request.get("level"))
        
    def __setRecognitionLaunched(self, value):
        self.recognition_launched = value
    
    def launchRecognition(self):
        
        if self.recognition_launched:
            return
        
        #Get Recognition parameters
        request = self._getParamsForVideoReconignition()
        url = self.new_camera_url.text()
        if not url:
            self.printError("No video selected !")
            return 
        
        self.btn_try_cameras.setEnabled(False)
        self.btn_add_camera.setEnabled(False)
        
        self.recognition_launched = True
        
        #Launch thread
        self.reconizer_worker = Worker(lambda: self._videoReconignition(url, request))
        self.reconizer_thread = QThread()
        
        self.reconizer_worker.moveToThread(self.reconizer_thread)
        
        self.reconizer_thread.started.connect(self.reconizer_worker.run)
        self.reconizer_worker.finished.connect(self.reconizer_thread.quit)
        self.reconizer_worker.finished.connect(lambda: self.__setRecognitionLaunched(False))
        self.reconizer_worker.finished.connect(self.reconizer_worker.deleteLater)
        self.reconizer_worker.error_occured.connect(self.printError)

        # Start the thread
        self.reconizer_thread.start()
        QMessageBox.information(self, self._translate("Title", "Started"),
                                self._translate("InfoMessage", "The recognition process started..."))

        
    
    def _videoReconignition(self, url, request: Request):
        assert isinstance(url, str)
        
        if not os.path.exists(url):
            raise ValueError("[Error] The video doesn't exist !")
        
        try:
            video = cv2.VideoCapture(url)

            #Utils
            __face_reconizer = FaceReconizer(concerned_disciplines=request.get("disciplines"),
                                             level= request.get("level"))
            __list_formatter = ListFormatter(request)

            result: list = []        
            students: set = {}

            start_time = ctime()

            while video.isOpened():

                is_frame_ready, frame = video.read()
                
                if is_frame_ready:
                    
                    try:
                        frame = cv2.resize(frame, (0,0), fx= 0.25, fy= 0.25)    
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    except:
                        pass
                    
                    students_detected: set = __face_reconizer.StudentsDetected(frame)

                    if students_detected:
                        temp = []
                        temp.extend(students_detected)
                        temp.extend(students) 
                        
                        students = set(temp) #We add students
                
                    else:

                        if students:
                            #When we are done looking for students for a period of time
                            time = ctime()
                            result.append({
                                "time": time,
                                "students": set(students)
                            })

                        students = {}

                    sleep(.2)
                    #Restart the timer eventually
                else:
                    break
            
            end_time = ctime()

            attendance_list = __list_formatter.FormattedList(result)

            attendance_list["start_time"] = start_time
            attendance_list["end_time"] = end_time
            attendance_list["course"] = request["course"]

            print("Attendance List : ")
            pprint(attendance_list)

            #Save attendance_list
            ROOT_DIR = os.path.dirname( os.path.dirname(__file__))
            FILE_ATTENDANCE_LIST = os.path.join(ROOT_DIR, "log/", f"attendance_list_{ctime()}.txt")
            
            try:
                with open(FILE_ATTENDANCE_LIST, "w") as f:
                    f.write( f"""\n ================ Attendance list {ctime()}======================== \n"""
                        + json.dumps(attendance_list, indent=4)
                    )
                    
            except:
                raise ValueError("Coudn't save the attendance list from the video, sorry :(")
            
        except: 
            raise ValueError("Something uninspect occur :(")
    
    def setCameraRunning(self, value):
        self.camera_is_running = value
    
    def _tryCameras(self):
        selectedItems = self.table_camera.selectedItems()

        if self.camera_is_running:
            QMessageBox.warning(self, self._translate("Title", "Camera already running"),
                                self._translate("WarningMessage", "There is already a camera running !"))
            return

        self.camera_is_running = True

        if not selectedItems:
            QMessageBox.warning(self, self._translate("Title", "Empty selection"),
                                self._translate("WarningMessage", "There are no camera selected !"))
            return

        camera_url = selectedItems[1].text()
        
        # if self.try_camera_thread.isRunning():
        #     QMessageBox.critical(self, self._translate("ErrorTitle", "Error"),
        #                          self._translate("ErrorMessage", "A camera is already running, please close the proccess before."))
        #     return
        
        QMessageBox.information(self, self._translate("Title", "Test camera"),
                                self._translate("InfoMessage", "You should press Escape Key (Esc) to close the record!"))
    
        self.try_camera_worker = Worker(lambda: self.tryCamera(camera_url))
        self.try_camera_thread = QThread()
        
        self.try_camera_worker.moveToThread(self.try_camera_thread)
        
        self.try_camera_thread.started.connect(self.try_camera_worker.run)
        self.try_camera_worker.finished.connect(self.try_camera_thread.quit)
        self.try_camera_worker.finished.connect(lambda: self.setCameraRunning(False))
        self.try_camera_worker.finished.connect(self.try_camera_worker.deleteLater)
        self.try_camera_worker.error_occured.connect(self.printError)

        # Start the thread
        self.try_camera_thread.start()

        
    def tryCamera(self, camera_url):
        
        if not self.camera_is_running:
            
            self.btn_try_cameras.setEnabled(False)
            self.btn_try_cameras.setText("Running...")    
            self.camera_is_running = True
            
            if camera_url == "Webcam":
                camera_url = 0
        
            camera = cv2.VideoCapture(camera_url)
            
            if camera.isOpened():
                
                while True:
                    
                    is_frame_ready, frame = camera.read()
                    
                    if is_frame_ready:
                        
                        cv2.imshow("Camera preview", frame)
                            
                    key = cv2.waitKey(20)
                    
                    sleep(.01)
                    
                    if key == 27: #Esc
                        break
                    
                cv2.destroyWindow("Camera preview")

            else:
                self.camera_is_running = False
                self.btn_try_cameras.setEnabled(True)
                self.btn_try_cameras.setText("Try")    
                raise ValueError("Impossible to join the camera, please make sure that the camera or the url is available !")
            
            camera.release()
            self.camera_is_running = False
            self.btn_try_cameras.setEnabled(True)
            self.btn_try_cameras.setText("Try")    
    
    
    def _updateCamerasList(self, classroom_name: str):
        assert isinstance(classroom_name, str)
        
        self.table_camera.clearContents()
        
        if classroom_name == "Local File":
            self.label_add_camera.setText(self._translate("Label", "Path"))
            self.new_camera_url.setEnabled(False)
            self.btn_delete_camera.setEnabled(False)
            self.btn_try_cameras.setEnabled(False)
            self.btn_try_cameras.setText(self._translate("Button", "Start"))
            if self.recognition_launched:
                self.btn_try_cameras.setText(self._translate("Button", "Running..."))
                self.btn_try_cameras.setEnabled(False)
                
            self.btn_add_camera.setText(self._translate("Button", "Select"))
            
            try:
                self.btn_try_cameras.clicked.connect(self.launchRecognition)
                self.btn_try_cameras.clicked.disconnect(self._tryCameras)
                self.btn_add_camera.clicked.disconnect(self._addCamera)
                self.btn_add_camera.clicked.connect(self.chooseVideoToReconize)
            except:
                pass
            
            return
        
        else:
            self.label_add_camera.setText(self._translate("Label", "Add new camera URL"))
            self.new_camera_url.setEnabled(True)
            self.btn_delete_camera.setEnabled(True)
            self.btn_try_cameras.setEnabled(True)
            self.btn_try_cameras.setText(self._translate("Button", "Try"))
            self.btn_add_camera.setText(self._translate("Button", "Add"))
            
            try:
                self.btn_try_cameras.clicked.disconnect(self.launchRecognition)
                self.btn_try_cameras.clicked.connect(self._tryCameras)
                self.btn_add_camera.clicked.connect(self._addCamera)
                self.btn_add_camera.clicked.disconnect(self.chooseVideoToReconize)
            
            except:
                pass
            
        classroom = Classroom(classroom_name)
        cameras = classroom.getCameras()
        
        for row_id in range(len(cameras)):
            try:
                self.table_camera.removeRow(row_id)
            except:
                pass
            
            self.table_camera.insertRow(row_id)
            
            camera_name = str(cameras[row_id].get("name"))
            camera_url = str(cameras[row_id].get("url")) 
            
            if camera_url.isdigit():
                camera_url = "Webcam"
            
            tw_item_name = QTableWidgetItem(camera_name)
            tw_item_name.classroom = classroom
            
            tw_item_url = QTableWidgetItem(camera_url)
            tw_item_url.classroom = classroom
            
            self.table_camera.setItem(row_id,
                                        0,
                                        tw_item_name)
            self.table_camera.setItem(row_id,
                                        1,
                                        tw_item_url)
        
        self.new_camera_url.clear()
            
    def chooseVideoToReconize(self):
        files = QFileDialog.getOpenFileName(self,
                                     "Select one file to open",
                                     "",
                                     "Videos (*.mp4 *.mkv *.avi)")
        
        try:
            video_path = files[0].replace("/", "\\")
        
            if video_path:
                self.btn_try_cameras.setEnabled(True)
                self.new_camera_url.setText(video_path)    
        except:
            pass

    
    def _addCamera(self):
        
        url = self.new_camera_url.text()
        
        if not url:
            QMessageBox.warning(self, self._translate("Title", "Empty url"),
                                                 self._translate(
                                                     "WarningMessage", "We coudn't add empty url"),
                                                 QMessageBox.Ok)
            return

        classroom = Classroom(self.select_classroom.currentText())
        classroom.addCamera(url)

        self._updateCamerasList(classroom['name'])
        
    #
    # --> Page Settings
    #
    def _refreshSettings(self):
        self.old_password.clear()
        self.new_password.clear()
        self.confirm_new_password.clear()
        
    def _updateAccount(self):
        
        username_pattern = r"^[a-zA-Z].*"
        password_pattern = r"........(.)*" #08 characters at least
        
        username = self.username_settings.text()
        old_password = hashlib.md5(bytes(self.old_password.text(), 'utf8'))\
                              .hexdigest()
        new_password = self.new_password.text()
        confirm_new_password = self.confirm_new_password.text()
        
        #Verifications
        if not re.match(username_pattern, username):
            QMessageBox.warning(self, self._translate("Title","Error"),
                                self._translate("ErrorMessage","Incorrect username format"))
            self._refreshSettings()
            return
        
        if self.admin_connected[2] != old_password:
            QMessageBox.warning(self, self._translate("Title","Error"),
                                self._translate("ErrorMessage","Incorrect password"))
            self._refreshSettings()
            return
            
        if not new_password and not confirm_new_password:
            try:
                DB.updateAdmin(self.admin_connected[0], 
                                username,
                                self.admin_connected[2])    
            except:
                QMessageBox.warning(self, self._translate("Title","Error"),
                                self._translate("ErrorMessage","Coudln't update the information :("))
                return
            
            else:
                QMessageBox.information(self, self._translate("Title", "Success"),
                                        self._translate("SuccessMessage","Update username success !"))
                
                id = self.admin_connected[0]
                self.admin_connected = (id, username, self.admin_connected[2])
                
                self._refreshSettings()
                return
                
        if not re.match(password_pattern, new_password):
            QMessageBox.warning(self, self._translate("Title","Error"),
                                self._translate("ErrorMessage","Incorrect new password format"))
            self._refreshSettings()
            return
        
        if new_password != confirm_new_password:
            QMessageBox.warning(self, self._translate("Title","Error"),
                                self._translate("ErrorMessage","The new password and the confirmation must be the same !"))
            self._refreshSettings()
            return
    
        new_password = hashlib.md5(bytes(new_password, 'utf8'))\
                              .hexdigest()
                              
        try:
            DB.updateAdmin(self.admin_connected[0], 
                            username,
                            new_password)
    
        except:
            QMessageBox.warning(self, self._translate("Title","Error"),
                            self._translate("ErrorMessage","Coudln't update the information :("))
            return
        
        else:
            QMessageBox.information(self, self._translate("Title", "Success"),
                                    self._translate("SuccessMessage","Update success !"))
            
            id = self.admin_connected[0]
            self.admin_connected = (id, username, new_password)
            
            self._refreshSettings()
            
            