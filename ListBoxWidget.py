from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.itemsList = set()        

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
           event.setDropAction(Qt.CopyAction)
           event.accept()
        else:
            event.ignore()
            

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    localFile = str(url.toLocalFile())

                    if localFile.endswith((".png", ".jpg", ".jpeg")):
                       self.itemsList.add(localFile)
                else:
                    continue
            
            self.clear()
            self.addItems(self.itemsList)
        else:
            event.ignore()


