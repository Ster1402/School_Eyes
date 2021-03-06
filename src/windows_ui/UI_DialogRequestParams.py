# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/UI_DialogRequestParams.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(909, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(773, 450))
        Dialog.setMaximumSize(QtCore.QSize(909, 450))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background: #002A44;\n"
"color: #dedede;")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Cameroon))
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(260, 20, 401, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(150, 35))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: #dedede;\n"
"background: transparent;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 400, 571, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_confirm_request = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_confirm_request.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_confirm_request.sizePolicy().hasHeightForWidth())
        self.btn_confirm_request.setSizePolicy(sizePolicy)
        self.btn_confirm_request.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_confirm_request.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_confirm_request.setFont(font)
        self.btn_confirm_request.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirm_request.setStyleSheet("QPushButton {\n"
"    color: #dedede;\n"
"    background: #002A44;\n"
"    border: 2px solid #dedede;\n"
"    border-radius: 15px;\n"
"    padding: 1px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #003c5f;\n"
"    border-color: #F38533;\n"
"}\n"
"\n"
"QPushButton:!enabled\n"
"{\n"
"     background-color: #004c5f;\n"
"        border-right: 5px solid #dedede;\n"
"        border-left: 5px solid #dedede;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #F38533;\n"
"}")
        self.btn_confirm_request.setObjectName("btn_confirm_request")
        self.horizontalLayout_2.addWidget(self.btn_confirm_request)
        self.btn_cancel_request = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_cancel_request.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel_request.sizePolicy().hasHeightForWidth())
        self.btn_cancel_request.setSizePolicy(sizePolicy)
        self.btn_cancel_request.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_cancel_request.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel_request.setFont(font)
        self.btn_cancel_request.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel_request.setStyleSheet("QPushButton {\n"
"    color: #dedede;\n"
"    background: rgb(179, 32, 27);\n"
"    border: 2px solid #dedede;\n"
"    border-radius: 15px;\n"
"    padding: 1px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #F38533;\n"
"}\n"
"\n"
"\n"
"QPushButton:!enabled\n"
"{\n"
"     background-color: #A03c5f;\n"
"        border-right: 5px solid #dedede;\n"
"        border-left: 5px solid #dedede;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #F38533;\n"
"}")
        self.btn_cancel_request.setObjectName("btn_cancel_request")
        self.horizontalLayout_2.addWidget(self.btn_cancel_request)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 80, 837, 290))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_classroom = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_classroom.sizePolicy().hasHeightForWidth())
        self.label_classroom.setSizePolicy(sizePolicy)
        self.label_classroom.setMinimumSize(QtCore.QSize(100, 35))
        self.label_classroom.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_classroom.setFont(font)
        self.label_classroom.setStyleSheet("color: #dedede;\n"
"background: transparent;")
        self.label_classroom.setObjectName("label_classroom")
        self.horizontalLayout_5.addWidget(self.label_classroom)
        self.select_classroom = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_classroom.sizePolicy().hasHeightForWidth())
        self.select_classroom.setSizePolicy(sizePolicy)
        self.select_classroom.setMinimumSize(QtCore.QSize(250, 35))
        self.select_classroom.setMaximumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.select_classroom.setFont(font)
        self.select_classroom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_classroom.setStyleSheet("QComboBox {\n"
"    padding: 0 15px 0 27px;\n"
"    border: 2px solid #dedede;\n"
"    color: #dedede;\n"
"    background: transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #dedede;\n"
"    padding: 10px;\n"
"    selection-background-color: #F38533;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #F38533;\n"
"}\n"
"\n"
"")
        self.select_classroom.setObjectName("select_classroom")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.select_classroom.addItem("")
        self.horizontalLayout_5.addWidget(self.select_classroom)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.student_level_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_level_label.sizePolicy().hasHeightForWidth())
        self.student_level_label.setSizePolicy(sizePolicy)
        self.student_level_label.setMinimumSize(QtCore.QSize(100, 35))
        self.student_level_label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.student_level_label.setFont(font)
        self.student_level_label.setStyleSheet("color: #dedede;\n"
"background: transparent;")
        self.student_level_label.setObjectName("student_level_label")
        self.horizontalLayout.addWidget(self.student_level_label)
        self.level_spinBox = QtWidgets.QSpinBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.level_spinBox.sizePolicy().hasHeightForWidth())
        self.level_spinBox.setSizePolicy(sizePolicy)
        self.level_spinBox.setMinimumSize(QtCore.QSize(250, 35))
        self.level_spinBox.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.level_spinBox.setFont(font)
        self.level_spinBox.setStyleSheet("QSpinBox {\n"
"    padding: 0 15px 0 27px;\n"
"    border: 2px solid #dedede;\n"
"    color: #dedede;\n"
"    background: transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QSpinBox:hover, QSpinBox:focus {\n"
"    border-color: #F38533;\n"
"}")
        self.level_spinBox.setMinimum(1)
        self.level_spinBox.setMaximum(5)
        self.level_spinBox.setObjectName("level_spinBox")
        self.horizontalLayout.addWidget(self.level_spinBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.table_discipline_axe = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_discipline_axe.sizePolicy().hasHeightForWidth())
        self.table_discipline_axe.setSizePolicy(sizePolicy)
        self.table_discipline_axe.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.table_discipline_axe.setStyleSheet("*{\n"
"    background: #003C5F;\n"
"    font-size: 16px;\n"
"    color: #dedede;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background: #002A44;\n"
"    border-radius: 5px;\n"
"    border-bottom: 2px solid #dedede;\n"
"    border-left: 1px solid #dedede;\n"
"    border-right: 1px solid #dedede;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    background-color: #F38533;\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #002A44;\n"
"    border-radius: 0;\n"
"    border-left: 1px solid #003C5F;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    background: #002A44;\n"
"    border-left: 1px solid #003c5f;\n"
"    color: #dedede;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QTableView::item:hover, QTableView::item:selected, QTableView::item:focus {\n"
"    background: #003c5f;\n"
"    color: #dedede;\n"
"}\n"
"")
        self.table_discipline_axe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_discipline_axe.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_discipline_axe.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_discipline_axe.setAlternatingRowColors(False)
        self.table_discipline_axe.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_discipline_axe.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_discipline_axe.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_discipline_axe.setGridStyle(QtCore.Qt.NoPen)
        self.table_discipline_axe.setWordWrap(True)
        self.table_discipline_axe.setCornerButtonEnabled(True)
        self.table_discipline_axe.setObjectName("table_discipline_axe")
        self.table_discipline_axe.setColumnCount(2)
        self.table_discipline_axe.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_discipline_axe.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_discipline_axe.setHorizontalHeaderItem(1, item)
        self.table_discipline_axe.horizontalHeader().setCascadingSectionResizes(True)
        self.table_discipline_axe.horizontalHeader().setDefaultSectionSize(400)
        self.table_discipline_axe.horizontalHeader().setStretchLastSection(True)
        self.table_discipline_axe.verticalHeader().setVisible(False)
        self.table_discipline_axe.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.table_discipline_axe)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.student_discipline_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_discipline_label.sizePolicy().hasHeightForWidth())
        self.student_discipline_label.setSizePolicy(sizePolicy)
        self.student_discipline_label.setMinimumSize(QtCore.QSize(100, 35))
        self.student_discipline_label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.student_discipline_label.setFont(font)
        self.student_discipline_label.setStyleSheet("color: #dedede;\n"
"background: transparent;")
        self.student_discipline_label.setObjectName("student_discipline_label")
        self.horizontalLayout_3.addWidget(self.student_discipline_label)
        self.discipline_comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discipline_comboBox.sizePolicy().hasHeightForWidth())
        self.discipline_comboBox.setSizePolicy(sizePolicy)
        self.discipline_comboBox.setMinimumSize(QtCore.QSize(150, 35))
        self.discipline_comboBox.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.discipline_comboBox.setFont(font)
        self.discipline_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.discipline_comboBox.setStyleSheet("QComboBox {\n"
"    padding: 0 15px 0 27px;\n"
"    border: 2px solid #dedede;\n"
"    color: #dedede;\n"
"    background: transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #dedede;\n"
"    padding: 10px;\n"
"    selection-background-color: #F38533;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #F38533;\n"
"}\n"
"\n"
"")
        self.discipline_comboBox.setObjectName("discipline_comboBox")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.discipline_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.discipline_comboBox)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.student_axe_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.student_axe_label.sizePolicy().hasHeightForWidth())
        self.student_axe_label.setSizePolicy(sizePolicy)
        self.student_axe_label.setMinimumSize(QtCore.QSize(100, 35))
        self.student_axe_label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.student_axe_label.setFont(font)
        self.student_axe_label.setStyleSheet("color: #dedede;\n"
"background: transparent;")
        self.student_axe_label.setObjectName("student_axe_label")
        self.horizontalLayout_4.addWidget(self.student_axe_label)
        self.axe_comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axe_comboBox.sizePolicy().hasHeightForWidth())
        self.axe_comboBox.setSizePolicy(sizePolicy)
        self.axe_comboBox.setMinimumSize(QtCore.QSize(150, 35))
        self.axe_comboBox.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.axe_comboBox.setFont(font)
        self.axe_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.axe_comboBox.setStyleSheet("QComboBox {\n"
"    padding: 0 15px 0 27px;\n"
"    border: 2px solid #dedede;\n"
"    color: #dedede;\n"
"    background: transparent;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #dedede;\n"
"    padding: 10px;\n"
"    selection-background-color: #F38533;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #F38533;\n"
"}\n"
"\n"
"")
        self.axe_comboBox.setObjectName("axe_comboBox")
        self.horizontalLayout_4.addWidget(self.axe_comboBox)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.btn_add_axe = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_axe.sizePolicy().hasHeightForWidth())
        self.btn_add_axe.setSizePolicy(sizePolicy)
        self.btn_add_axe.setMinimumSize(QtCore.QSize(110, 30))
        self.btn_add_axe.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_axe.setFont(font)
        self.btn_add_axe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_axe.setStyleSheet("QPushButton {\n"
"    color: #dedede;\n"
"    background: #002A44;\n"
"    border: 2px solid #dedede;\n"
"    border-radius: 15px;\n"
"    padding: 1px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #003c5f;\n"
"    border-color: #F38533;\n"
"}\n"
"\n"
"\n"
"QPushButton:!enabled\n"
"{\n"
"     background-color: #004c5f;\n"
"        border-right: 5px solid #dedede;\n"
"        border-left: 5px solid #dedede;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #F38533;\n"
"}")
        self.btn_add_axe.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Cameroon))
        self.btn_add_axe.setObjectName("btn_add_axe")
        self.horizontalLayout_7.addWidget(self.btn_add_axe)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update Student"))
        self.title_label.setText(_translate("Dialog", "Recognition parameters"))
        self.btn_confirm_request.setText(_translate("Dialog", "Confirm"))
        self.btn_cancel_request.setText(_translate("Dialog", "Cancel"))
        self.label_classroom.setText(_translate("Dialog", "Classroom"))
        self.select_classroom.setPlaceholderText(_translate("Dialog", "-- Discipline --"))
        self.select_classroom.setItemText(0, _translate("Dialog", "GIT"))
        self.select_classroom.setItemText(1, _translate("Dialog", "TTIC"))
        self.select_classroom.setItemText(2, _translate("Dialog", "GP"))
        self.select_classroom.setItemText(3, _translate("Dialog", "GAM"))
        self.select_classroom.setItemText(4, _translate("Dialog", "ROI"))
        self.select_classroom.setItemText(5, _translate("Dialog", "GESI"))
        self.select_classroom.setItemText(6, _translate("Dialog", "GC"))
        self.select_classroom.setItemText(7, _translate("Dialog", "TAU"))
        self.student_level_label.setText(_translate("Dialog", "Level"))
        self.table_discipline_axe.setSortingEnabled(True)
        item = self.table_discipline_axe.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Disciplines"))
        item = self.table_discipline_axe.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Axes"))
        self.student_discipline_label.setText(_translate("Dialog", "Discipline"))
        self.discipline_comboBox.setPlaceholderText(_translate("Dialog", "-- Discipline --"))
        self.discipline_comboBox.setItemText(0, _translate("Dialog", "GIT"))
        self.discipline_comboBox.setItemText(1, _translate("Dialog", "TTIC"))
        self.discipline_comboBox.setItemText(2, _translate("Dialog", "GP"))
        self.discipline_comboBox.setItemText(3, _translate("Dialog", "GAM"))
        self.discipline_comboBox.setItemText(4, _translate("Dialog", "ROI"))
        self.discipline_comboBox.setItemText(5, _translate("Dialog", "GESI"))
        self.discipline_comboBox.setItemText(6, _translate("Dialog", "GC"))
        self.discipline_comboBox.setItemText(7, _translate("Dialog", "TAU"))
        self.student_axe_label.setText(_translate("Dialog", "Axe"))
        self.axe_comboBox.setPlaceholderText(_translate("Dialog", "-- Axe --"))
        self.btn_add_axe.setText(_translate("Dialog", "Add"))
