from src.model.Classroom import Classroom
from src.database.db import DisciplineModel
from src.windows_ui.UI_DialogRequestParams import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QCoreApplication


class DiaglogRequestParams(Ui_Dialog, QDialog):

    def __init__(self, parent):

        super().__init__(parent)

        self.setupUi(self)
        self.retranslateUi(self)

        self.__translate = QCoreApplication.translate

        self.setWindowTitle(self.__translate("Title", "Request parameters"))

        self.request = {
            "classroom": "",
            "level": 0,
            "disciplines": []
        }

        # Informations
        self._getInformations()

        # Slots connections
        self.__slots_connection()

    # Slots
    def __slots_connection(self):
        self.discipline_comboBox.currentTextChanged.connect(
            lambda: self._updateAxes())
        self.btn_confirm_request.clicked.connect(
            lambda: self.__confirmRequest()
        )
        self.btn_cancel_request.clicked.connect(self.reject)
        self.btn_add_axe.clicked.connect(
            lambda: self.__addAxe()
        )

    # Informations
    def _getInformations(self):
        self.select_classroom.clear()
        classrooms = Classroom.getClassroomsList()
        classrooms.remove("Local File")
        self.select_classroom.addItems(classrooms)
        
        self.table_discipline_axe.clearContents()

        # Get disciplines
        self.discipline_comboBox.clear()
        self.discipline_comboBox.addItems(
            DisciplineModel.getDisciplinesName()
        )

    # Print warning
    def printWarning(self, title, warning):
        QMessageBox.warning(self,
                            self.__translate("Title", title),
                            self.__translate('WarningText', warning))

    # Add axe
    def __addAxe(self):

        discipline_name = self.discipline_comboBox.currentText()
        axe_name = self.axe_comboBox.currentText()

        if not self.request["disciplines"]:
            self.request["disciplines"].append(
                {
                    "name": discipline_name,
                    "axes": [axe_name]
                }
            )

        else:

            discipline_found = False
            for discipline in self.request['disciplines']:

                if discipline.get("name") == discipline_name:
                    discipline_found = True
                    if axe_name not in discipline.get("axes"):
                        discipline["axes"].append(axe_name)

            if not discipline_found:
                self.request["disciplines"].append({
                    "name": discipline_name,
                    "axes": [axe_name]
                })

        i = 0

        self.table_discipline_axe.clearContents()
        for discipline in self.request.get("disciplines"):
            try:
                self.table_discipline_axe.removeRow(i)
            except:
                pass
            
            self.table_discipline_axe.insertRow(i)
            self.table_discipline_axe.setItem(i, 0, QTableWidgetItem(discipline["name"]))
            self.table_discipline_axe.setItem(i, 1, QTableWidgetItem(' - '.join(discipline["axes"])))
            i += 1

    # Update axes
    def _updateAxes(self):
        discipline = self.discipline_comboBox.currentText()

        # Check level

        if discipline == "TCO":
            self.level_spinBox.setMaximum(2)
            self.level_spinBox.setMinimum(1)
            self.axe_comboBox.setEnabled(False)
        else:
            self.level_spinBox.setMaximum(5)
            self.level_spinBox.setMinimum(3)
            self.axe_comboBox.setEnabled(True)

        # Update axe
        self.axe_comboBox.clear()
        self.axe_comboBox.addItems(
            DisciplineModel.getAxes(discipline))

        if self.axe_comboBox.count() > 0:
            self.axe_comboBox.setCurrentIndex(0)

    # Confirm request
    def __confirmRequest(self):
        
        classroom = self.select_classroom.currentText()
        
        if not classroom:
            self.printWarning("Field empty", "Classroom field can't be empty")
            return
        
        level = self.level_spinBox.value()
        
        if not self.request['disciplines']:
            self.printWarning("Field empty", "No discipline selected !")
            return
            
        self.request['level'] = level
        self.request["classroom"] = f"_{classroom}"
        
        self.accept()