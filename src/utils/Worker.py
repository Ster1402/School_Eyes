
import hashlib
import re
from time import sleep
from PyQt5.QtCore import QObject, pyqtSignal

class Worker(QObject):
    finished = pyqtSignal()
    error_occured = pyqtSignal(str)
    
    def __init__(self, func):
        super().__init__()
        self.function = func
    
    def run(self):
        try:
            self.function()
        except ValueError as err:
            self.error_occured.emit(str(err))
            
        self.finished.emit()
