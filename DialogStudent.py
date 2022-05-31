
from src.utils.Worker import Worker
from UI_DialogStudent import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from src.database.db import DisciplineModel, StudentModel
from PyQt5.QtCore import QCoreApplication, QThread

class DiaglogStudent(Ui_Dialog, QDialog):
    
    def __init__(self, parent, student_register_number):
        
        super().__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)
        
        self.student_register_number = student_register_number
        self.__translate = QCoreApplication.translate
        
        self.setWindowTitle(self.__translate("Title", "Update Informations"))
        
        #Student informations
        self._getStudentInformations()
        
        #Slots connections
        self.__slots_connection()
        
    def __slots_connection(self):
        self.btn_update_student.clicked.connect(lambda: self.threadUpdateStudent())
        self.btn_cancel_update_student.clicked.connect(lambda: self.reject())
        self.student_discipline_comboBox.currentTextChanged.connect(lambda discipline: self._updateAxes(discipline))
        self.btn_remove_picture.clicked.connect(lambda: self.removeStudentSelectedPictures())
        self.btn_select_pictures.clicked.connect(lambda: self.chooseStudentPictures())
        
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
        
    def _updateAxes(self, discipline):
        
        self._on_discipline_changed()
        
        self.student_axe_comboBox.clear()
        self.student_axe_comboBox.addItems(DisciplineModel.getAxes(discipline))
        
        if self.student_axe_comboBox.count() > 0:
            self.student_axe_comboBox.setCurrentIndex(0)
    
    def chooseStudentPictures(self):
        files = QFileDialog.getOpenFileNames(self,
                                     "Select one or more files to open",
                                     "",
                                     "Images (*.png *.jpeg *.jpg)")
        pictures_path = files[0]
        pictures_path = [ path.replace("/", "\\") for path in pictures_path ]
        self.drag_and_drop_box.itemsList.update(pictures_path)
        self.drag_and_drop_box.clear()
        self.drag_and_drop_box.addItems(self.drag_and_drop_box.itemsList)
        
    def removeStudentSelectedPictures(self):
        
        selectedItems = self.drag_and_drop_box.selectedItems()
        
        if not selectedItems:
            QMessageBox.information(self, self.__translate("Title", "No selection"),
                                    self.__translate("WarningMessage", "No picture selected"))
            return
        
        if QMessageBox.Ok != QMessageBox.warning(self, self.__translate("Title", "Delete"),
                                    self.__translate("WarningMessage", "Are you sure that you want to delete these pictures ?"),
                                    QMessageBox.Ok | QMessageBox.Cancel):
            return
        
        for selectedItem in selectedItems:
            
            self.drag_and_drop_box.takeItem(self.drag_and_drop_box.row(selectedItem))
            
            items = [self.drag_and_drop_box.item(i) for i in range(self.drag_and_drop_box.count())]
            items = set( [item.text() for item in items] )
            self.drag_and_drop_box.itemsList = items
            
            StudentModel.removePicture(selectedItem.text())
            
    def _getStudentInformations(self):
        self.student = StudentModel.findStudent(self.student_register_number)
        
        self.drag_and_drop_box.clear()
        self.drag_and_drop_box.addItems(self.student['pictures'])
        self.drag_and_drop_box.itemsList = set(self.student['pictures'])
        
        name, surname = self.student['name'].split(" _ ")
        
        self.student_name_lineEdit.setText(name)
        self.student_surname_lineEdit.setText(surname)
        self.student_register_number_lineEdit.setText(self.student['register_number'])
        
        self.student_discipline_comboBox.clear()
        self.student_discipline_comboBox.addItems(DisciplineModel.getDisciplinesName())
        self.student_discipline_comboBox.setCurrentText(self.student['discipline']) #...
        
        self.student_axe_comboBox.clear()
        self.student_axe_comboBox.addItems(DisciplineModel.getAxes(self.student['discipline']))
        self.student_axe_comboBox.setCurrentText(self.student['axe'])

        self.student_level_spinBox.setValue(self.student['level'])

    def __empytFieldWarning(self, field: str) -> None:
       
        dialog = QMessageBox(self) 
        dialog.setWindowTitle(self.__translate("Title", "Empty Field"))
        dialog.setText(self.__translate("WarningMessage", 
                                                  f"{field} field can not be empty !"))                              
        dialog.setIcon(QMessageBox.Warning)

        dialog.exec()

    def updateStudent(self):
        
        name = self.student_name_lineEdit.text()
        #Verification
        if not name:
            self.__empytFieldWarning("Name")
            return
        
        surname = self.student_surname_lineEdit.text()
        level = self.student_level_spinBox.value()
        axe = self.student_axe_comboBox.currentText()
        #Verification
        if not axe:
            self.__empytFieldWarning("Axe")
            return
        
        register_number = self.student_register_number_lineEdit.text()
        #Verification
        if not register_number:
            self.__empytFieldWarning("Register Number")
            return
            
        pictures = self.drag_and_drop_box.itemsList
        
        new_student = {"name" : name + " _ " + surname, 
                       "level": level, 
                       "axe": axe,
                       "pictures" : pictures,
                       "register_number" : register_number}
        
        
        self.student.update(new_student)
        
        try:
            StudentModel.updateStudent(self.student, axe)
            
            for picture in pictures:

                try:
                    StudentModel.addStudentPicture(picture, register_number)
                except ValueError:
                    raise ValueError(f"""Error trying to add the picture : \n"""
                                                        f"""Path : {picture}""")
                    # QMessageBox.warning(self, self.__translate("Title", "Error"),
                    #                     self.__translate("ErrorMessage", f"""Error trying to add the picture : \n"""
                    #                                     f"""Path : {picture}"""))
                
        except ValueError:
            QMessageBox.critical(self, self.__translate("Title","Error"),
                                 self.__translate("ErrorMessage", "Sorry, an error occur. :( "))
            self.reject()
        else:
            QMessageBox.information(self, self.__translate("Title","Success"),
                                 self.__translate("SuccessMessage", "Update is done !"))
            self.accept()
            
            
    def threadUpdateStudent(self):
        
        confirm_dialog = QMessageBox(self) 
        confirm_dialog.setWindowTitle(self.__translate("Title", "Update Student"))
        confirm_dialog.setText(self.__translate("WarningMessage", 
                                                  "Are you sure that you want to update the informations ? "))                              
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        if not confirm_dialog.exec() == QMessageBox.Yes:
            return
        
        self.loader = QMessageBox(self)
        self.loader.setWindowTitle("Processing...")
        self.loader.setText("Process running, please wait...")
        self.loader.exec()

        self.success_message = QMessageBox(self)
        self.success_message.setWindowTitle(self.__translate("Title", "Success")) 
        self.success_message.setText(self.__translate("InfoMessage", "Student successfully updated !"))

        self.btn_update_student.setEnabled(False)
        
        self.update_student_worker = Worker(lambda: self.updateStudent())
        self.update_student_thread = QThread()
        
        self.update_student_worker.moveToThread(self.update_student_thread)
        
        self.update_student_thread.started.connect(self.update_student_worker.run)
        self.update_student_thread.started.connect(lambda: self.loader.setEnabled(False))
        self.update_student_worker.finished.connect(self.update_student_thread.quit)
        self.update_student_worker.finished.connect(self.update_student_worker.deleteLater)
        self.update_student_worker.finished.connect(lambda: self.loader.setEnabled(True))
        self.update_student_worker.finished.connect(lambda: self.btn_update_student.setEnabled(True))
        self.update_student_worker.finished.connect(lambda: self.success_message.exec())
        self.update_student_worker.error_occured.connect(self.printError)

        # Start the thread
        self.update_student_thread.start()
        
    def printError(self, error: str):
        QMessageBox.critical(self, self.__translate("Title", "Error"),
                                self.__translate("ErrorMessage", error))
        
        