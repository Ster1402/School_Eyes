
import hashlib

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from database.db import DB
from model.Classroom import Classroom
from UI_MainWindows import Ui_MainWindow


class MainWindows(Ui_MainWindow, QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.retranslateUi(self)

        self._translate = QtCore.QCoreApplication.translate

        self.__initialize_pages_data()
        
        #Home windows
        self.__adminConnectionVerification()
        self.index()
        #Establishing slots connection
        self.__slots_connection()
        
        
    def index(self):
        #If the user is connected, show home widget
        if self.connected:
            self.showHome()
        else:
            self.logout()

    def showHome(self):
        self.activate_menu_button()
        self.stacked_widget.setCurrentWidget(self.page_home)

    def printLoginError(self):
        QMessageBox.warning(self, 
                          self._translate("LoginError","Login Error"),
                          self._translate("ErrorMessage", "We could'nt find the corresponding account,\
please make sure that the informations provide are correct."))

    def __adminConnectionVerification(self):
        #Check if an admin is connected
        self.admin_connected = DB.adminConnected()
        #If an admin is connected we have (id, login, password) in admin_connected
        
        self.connected = self.admin_connected != None  
            
    def login(self):
        #Check login and password
        login = self.username_login.text()
        password = hashlib.md5(bytes(self.password_login.text(), "utf8"))\
                          .hexdigest()
                          
        self.admin_connected = DB.checkIfAdminExist(login, password)
        
        if not self.admin_connected:
            self.printLoginError()
            self.password_login.clear()
        else:
            DB.connectAdmin(self.admin_connected[0])
            self.showHome()    

    def logout(self):
        self.activate_menu_button(False)
        self.password_login.clear()
        self.username_login.clear()
        self.stacked_widget.setCurrentWidget(self.page_login)

    def __slots_connection(self):   
        #
        # --> Home button clicked
        #
        self.btn_home_students.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_home_students))
        self.btn_home_camera.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_home_camera))
        self.btn_home_settings.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_home_settings))
        self.btn_home_help.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_home_help))
        #
        # --> Toggle menu clicked
        #
        self.show_menu = True
        self.btn_show_menu.clicked.connect(lambda: self.toggle_menu())
        #
        # --> Menu button clicked
        #
        self.btn_menu_home.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_menu_home))
        self.btn_menu_camera.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_menu_camera))
        self.btn_menu_students.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_menu_students))
        self.btn_menu_settings.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_menu_settings))
        self.btn_menu_help.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_menu_help))
        self.btn_menu_logout.clicked.connect(lambda: self.on_btn_home_clicked(self.btn_menu_logout))
        #
        # --> Page Login
        #
        self.confirm_login.clicked.connect(lambda: self.login())
        self.password_login.returnPressed.connect(lambda: self.login())
    
    def __initialize_pages_data(self):
        #
        # --> Classrooms : Camera page
        #
        
        self.table_camera.clearContents()
        
        classrooms_names = Classroom.getClassroomsList()
        self.classrooms = [ Classroom(name) for name in classrooms_names]
        self.select_classroom.clear()
        self.select_classroom.addItems(classrooms_names)
        
        self.select_classroom.setCurrentIndex(0)
        
        for classroom in self.classrooms:
            cameras = classroom.getCameras()
            rows_count = len(cameras)
            
            for row_id in range(rows_count):
                self.table_camera.setItem(row_id, 
                                          0, 
                                          QTableWidgetItem(cameras[row_id].get("name"))
                )
                self.table_camera.setItem(row_id, 
                                          1, 
                                          QTableWidgetItem(cameras[row_id].get("url"))
                )
                
    
    def on_btn_home_clicked(self, sender):
        
        if sender.objectName() == "btn_home_students" or sender.objectName() == "btn_menu_students":
            self.stacked_widget.setCurrentWidget(self.page_students)
        elif sender.objectName() == "btn_home_camera"  or sender.objectName() == "btn_menu_camera":
            self.stacked_widget.setCurrentWidget(self.page_camera)
        elif sender.objectName() == "btn_home_settings" or sender.objectName() == "btn_menu_settings":
            self.stacked_widget.setCurrentWidget(self.page_settings)
        elif sender.objectName() == "btn_home_help" or sender.objectName() == "btn_menu_help":
            self.stacked_widget.setCurrentWidget(self.page_help)
        elif sender.objectName() == "btn_menu_home":
            self.stacked_widget.setCurrentWidget(self.page_home)
        elif sender.objectName() == "btn_menu_logout":
            self.logout()
        
    def activate_menu_button(self, ok = True):
        self.btn_menu_home.setEnabled(ok)
        self.btn_menu_students.setEnabled(ok)
        self.btn_menu_camera.setEnabled(ok)
        self.btn_menu_help.setEnabled(True) #The help button is always active
        self.btn_menu_settings.setEnabled(ok)
        self.btn_menu_logout.setEnabled(ok)
        
        
    def toggle_menu(self):
        
        if self.show_menu:
        
            #Get width
            width = self.menu_left.width()
            maxEntend = 160
            standard_width = 70
            
            #Set Max Width
            if width == 70:
                widthExtended = maxEntend
            else:
                widthExtended = standard_width
                
            #Animation
            self.animation = QPropertyAnimation(self.menu_left, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.BezierSpline)
            self.animation.start()
            
            