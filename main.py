import sys
from PyQt5.QtWidgets import QApplication 
from MainWindows import MainWindows

def main(argv):    
    app = QApplication(argv)
    windows = MainWindows()
    windows.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv) 






