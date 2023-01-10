import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\beobs\\OneDrive\\Desktop\\Github\\Prac_QT\\4.notepad_assave\\pyqt_UI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFunction) #함수 추가,designer에서도 추가

        self.opened = False 
        self.open_file_path = ''

    def open_file(self,fname):
        with open(fname,encoding = 'UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)

        self.opened = True #open을 했으면 True처리
        self.open_file_path = fname #경로 가지고 있기

        print(fname)
        print("open")
    
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0] :
            self.open_file(fname[0])
          
    def save_file(self,fname):
        data = self.plainTextEdit.toPlainText()
        with open(fname,'w', encoding = 'UTF8') as f:
            f.write(data)
        self.opened = True 
        self.open_file_path = fname

        print(fname)
        print("save")        

    def saveFunction(self):
        if self.opened : #이미 한번 저장한적이 있으면 해당 path에 저장하고
            self.save_file(self.open_file_path)
        else : # 그게 아니면 다른이름의 저장이 뜨는것과 동일한 동작을 해야한다.
            self.saveAsFunction()

    def saveAsFunction(self):  
        fname = QFileDialog.getSaveFileName(self) #항상 탐색기가 열려야한다.
        if fname[0] :
            self.save_file(fname[0])
      

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()