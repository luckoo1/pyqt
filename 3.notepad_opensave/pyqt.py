import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\beobs\\OneDrive\\Desktop\\Github\\Prac_QT\\3.notepad_opensave\\pyqt_UI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)

    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self) #탐색기 열기하기(window 제공함수)
        if fname[0] : #fname에 저장된게 있다면
            data = self.plainTextEdit.toPlainText()
            with open(fname[0],encoding = 'UTF8') as f:
                data = f.read()
            self.plainTextEdit.setPlainText(data)
            print(fname[0]) #파일경로 출력
            print("open")

    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0] : #fname에 저장된게 없다면
            data = self.plainTextEdit.toPlainText()
            with open(fname[0],'w', encoding = 'UTF8') as f:
                f.write(data)
            print(fname[0]) #파일경로 출력
            print("save")

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()