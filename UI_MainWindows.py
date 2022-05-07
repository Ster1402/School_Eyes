# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_MainWindowsYMgLcp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 563)
        MainWindow.setMinimumSize(QSize(877, 500))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(45,45,45);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #002A44;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QFrame(self.centralwidget)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(877, 70))
        self.menu_bar.setMaximumSize(QSize(16777215, 40))
        self.menu_bar.setStyleSheet(u"background-color: #002A44;")
        self.menu_bar.setFrameShape(QFrame.NoFrame)
        self.menu_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.menu_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_btn_show_menu = QFrame(self.menu_bar)
        self.frame_btn_show_menu.setObjectName(u"frame_btn_show_menu")
        self.frame_btn_show_menu.setMinimumSize(QSize(70, 0))
        self.frame_btn_show_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_btn_show_menu.setStyleSheet(u"QFrame:hover {\n"
"	background-color: #002A44;\n"
"}")
        self.frame_btn_show_menu.setFrameShape(QFrame.NoFrame)
        self.frame_btn_show_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_btn_show_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_show_menu = QPushButton(self.frame_btn_show_menu)
        self.btn_show_menu.setObjectName(u"btn_show_menu")
        self.btn_show_menu.setMaximumSize(QSize(70, 16777215))
        self.btn_show_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_show_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/images/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	width: 100%;\n"
"	height: 100%; \n"
"	margin: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #003c5f;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #F38530;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_show_menu)


        self.horizontalLayout.addWidget(self.frame_btn_show_menu, 0, Qt.AlignLeft)

        self.frame_logo = QFrame(self.menu_bar)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setStyleSheet(u"background-color: rgb(0, 118, 186);")
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.logo = QFrame(self.frame_logo)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(0, 55))
        self.logo.setMaximumSize(QSize(80, 16777215))
        self.logo.setStyleSheet(u"image: url(:/logo/images/SchoolEyes_Logo.png);")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.logo)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame_logo)


        self.verticalLayout.addWidget(self.menu_bar, 0, Qt.AlignTop)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMaximumSize(QSize(16777215, 16777215))
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.body)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_left = QFrame(self.body)
        self.menu_left.setObjectName(u"menu_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_left.sizePolicy().hasHeightForWidth())
        self.menu_left.setSizePolicy(sizePolicy1)
        self.menu_left.setMaximumSize(QSize(70, 16777215))
        self.menu_left.setFrameShape(QFrame.NoFrame)
        self.menu_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_left)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.menu_left)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_home = QPushButton(self.frame)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_menu_home.sizePolicy().hasHeightForWidth())
        self.btn_menu_home.setSizePolicy(sizePolicy2)
        self.btn_menu_home.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_menu_home.setFont(font)
        self.btn_menu_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_home.setStyleSheet(u"QPushButton {\n"
"	color: #cecece;\n"
"	background-image: url(:/24x24/images/icons/24x24/cil-home.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid #002A44;\n"
"	border-right: 5px solid #002A44;\n"
"	background-color: #002A44;\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#003c5f;\n"
"	border-left: 25px solid #003c5f;\n"
"	border-right: 5px solid #F38530;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #F38530;\n"
"	border-left: 25px solid #F38530;\n"
"}\n"
"")
        self.btn_menu_home.setLocale(QLocale(QLocale.English, QLocale.Cameroon))

        self.verticalLayout_4.addWidget(self.btn_menu_home)

        self.btn_menu_students = QPushButton(self.frame)
        self.btn_menu_students.setObjectName(u"btn_menu_students")
        sizePolicy2.setHeightForWidth(self.btn_menu_students.sizePolicy().hasHeightForWidth())
        self.btn_menu_students.setSizePolicy(sizePolicy2)
        self.btn_menu_students.setMinimumSize(QSize(0, 80))
        self.btn_menu_students.setFont(font)
        self.btn_menu_students.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_students.setStyleSheet(u"QPushButton {\n"
"	color: #cecece;\n"
"	background-image: url(:/24x24/images/icons/24x24/cil-people.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid #002A44;\n"
"	border-right: 5px solid #002A44;\n"
"	background-color: #002A44;\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#003c5f;\n"
"	border-left: 25px solid #003c5f;\n"
"	border-right: 5px solid #F38530;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #F38530;\n"
"	border-left: 25px solid #F38530;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_menu_students)

        self.btn_menu_camera = QPushButton(self.frame)
        self.btn_menu_camera.setObjectName(u"btn_menu_camera")
        sizePolicy2.setHeightForWidth(self.btn_menu_camera.sizePolicy().hasHeightForWidth())
        self.btn_menu_camera.setSizePolicy(sizePolicy2)
        self.btn_menu_camera.setMinimumSize(QSize(0, 80))
        self.btn_menu_camera.setFont(font)
        self.btn_menu_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_camera.setStyleSheet(u"QPushButton {\n"
"	color: #cecece;\n"
"	background-image: url(:/24x24/images/icons/24x24/cil-video.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid #002A44;\n"
"	border-right: 5px solid #002A44;\n"
"	background-color: #002A44;\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#003c5f;\n"
"	border-left: 25px solid #003c5f;\n"
"	border-right: 5px solid #F38530;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #F38530;\n"
"	border-left: 25px solid #F38530;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.btn_menu_camera)

        self.btn_menu_settings = QPushButton(self.frame)
        self.btn_menu_settings.setObjectName(u"btn_menu_settings")
        sizePolicy2.setHeightForWidth(self.btn_menu_settings.sizePolicy().hasHeightForWidth())
        self.btn_menu_settings.setSizePolicy(sizePolicy2)
        self.btn_menu_settings.setMinimumSize(QSize(0, 80))
        self.btn_menu_settings.setFont(font)
        self.btn_menu_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_settings.setStyleSheet(u"QPushButton {\n"
"	color: #cecece;\n"
"	background-image: url(:/24x24/images/icons/24x24/cil-settings.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid #002A44;\n"
"	border-right: 5px solid #002A44;\n"
"	background-color: #002A44;\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#003c5f;\n"
"	border-left: 25px solid #003c5f;\n"
"	border-right: 5px solid #F38530;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #F38530;\n"
"	border-left: 25px solid #F38530;\n"
"}\n"
"")
        self.btn_menu_settings.setLocale(QLocale(QLocale.English, QLocale.Cameroon))

        self.verticalLayout_4.addWidget(self.btn_menu_settings)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.menu_bottom = QFrame(self.menu_left)
        self.menu_bottom.setObjectName(u"menu_bottom")
        sizePolicy1.setHeightForWidth(self.menu_bottom.sizePolicy().hasHeightForWidth())
        self.menu_bottom.setSizePolicy(sizePolicy1)
        self.menu_bottom.setMinimumSize(QSize(0, 150))
        self.menu_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.menu_bottom.setLocale(QLocale(QLocale.English, QLocale.Cameroon))
        self.menu_bottom.setFrameShape(QFrame.NoFrame)
        self.menu_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menu_bottom)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.btn_menu_help = QPushButton(self.menu_bottom)
        self.btn_menu_help.setObjectName(u"btn_menu_help")
        sizePolicy2.setHeightForWidth(self.btn_menu_help.sizePolicy().hasHeightForWidth())
        self.btn_menu_help.setSizePolicy(sizePolicy2)
        self.btn_menu_help.setMinimumSize(QSize(0, 80))
        self.btn_menu_help.setFont(font)
        self.btn_menu_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_help.setStyleSheet(u"QPushButton {\n"
"	color: #cecece;\n"
"	background-image: url(:/24x24/images/icons/24x24/cil-lightbulb.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid #002A44;\n"
"	border-right: 5px solid #002A44;\n"
"	background-color: #002A44;\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:#003c5f;\n"
"	border-left: 25px solid #003c5f;\n"
"	border-right: 5px solid #F38530;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #F38530;\n"
"	border-left: 25px solid #F38530;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.btn_menu_help)


        self.verticalLayout_3.addWidget(self.menu_bottom, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.menu_left)

        self.frame_content = QFrame(self.body)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: rgb(149, 186, 255);")
        self.frame_content.setLocale(QLocale(QLocale.English, QLocale.Cameroon))
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_content)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QStackedWidget(self.frame_content)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setLayoutDirection(Qt.LeftToRight)
        self.page_home.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.gridLayoutHome = QGridLayout()

        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()

        self.button1.setText(u"Button 1")
        self.button2.setText(u"Button 2")
        self.button3.setText(u"Button 3")

        self.gridLayoutHome.addWidget(self.button1)
        self.gridLayoutHome.addWidget(self.button2)
        self.gridLayoutHome.addWidget(self.button3)

        self.page_home.setLayout(self.gridLayoutHome)

        self.stacked_widget.addWidget(self.page_home)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.label = QLabel(self.page_login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 80, 91, 41))
        self.label_2 = QLabel(self.page_login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 180, 47, 13))
        self.label_3 = QLabel(self.page_login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 270, 47, 13))
        self.stacked_widget.addWidget(self.page_login)
        self.page_camera = QWidget()
        self.page_camera.setObjectName(u"page_camera")
        self.page_camera.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stacked_widget.addWidget(self.page_camera)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.page_help.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.stacked_widget.addWidget(self.page_help)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"background-color: rgb(135, 135, 135);")
        self.stacked_widget.addWidget(self.page_settings)
        self.page_students = QWidget()
        self.page_students.setObjectName(u"page_students")
        self.page_students.setStyleSheet(u"background-color: rgb(255, 61, 90);")
        self.stacked_widget.addWidget(self.page_students)

        self.verticalLayout_6.addWidget(self.stacked_widget)


        self.horizontalLayout_3.addWidget(self.frame_content)


        self.verticalLayout.addWidget(self.body)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"School Eyes", None))
        self.btn_show_menu.setText("")
        self.btn_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_menu_students.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.btn_menu_camera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.btn_menu_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_menu_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

