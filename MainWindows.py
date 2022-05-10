
from Ui_Windows import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

class MainWindows(Ui_MainWindow, QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        
        #Home windows
        self.index()
        #Establishing slots connection
        self.__slots_connection()
        
        self.activate_menu_button()

    def index(self):
        #If the user is connected, show home widget
        self.stacked_widget.setCurrentWidget(self.page_home)

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
            self.stacked_widget.setCurrentWidget(self.page_login)
        
    def activate_menu_button(self, ok = True):
        self.btn_menu_home.setEnabled(ok)
        self.btn_menu_students.setEnabled(ok)
        self.btn_menu_camera.setEnabled(ok)
        self.btn_menu_help.setEnabled(True) #The help button is always active
        self.btn_menu_settings.setEnabled(ok)
        self.btn_menu_logout.setEnabled(ok)
        
        
    def toggle_menu(self):
        pass