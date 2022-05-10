
import sys
from PyQt5.QtWidgets import QApplication 
from MainWindows import MainWindows

app = QApplication([])

windows = MainWindows()
windows.show()

sys.exit( app.exec_() )

