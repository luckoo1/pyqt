import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\beobs\\OneDrive\\Desktop\\Github\\Prac_QT\\2.notepad_menubar\\pyqt_UI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)

    def openFunction(self):
        print("open")

    def saveFunction(self):
        print("save")

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()