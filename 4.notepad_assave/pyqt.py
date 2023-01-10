import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Users\\beobs\\OneDrive\\Desktop\\Github\\Prac_QT\\6.notepad_MessageBox\\pyqt_UI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.close)

        self.opened = False 
        self.open_file_path = '제목 없음'
    
    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을{}에 저장하시겠습니까?".format(self.open_file_path))
        msgBox.exec_() #실행
        # msgBox.addButton()

    def closeEvent(self, event) :
        self.save_changed_data()
        print("Close")
        # event.ignore()

    def open_file(self,fname):
        with open(fname,encoding = 'UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)

        self.opened = True
        self.open_file_path = fname

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
        if self.opened :
            self.save_file(self.open_file_path)
        else :
            self.saveAsFunction()

    def saveAsFunction(self):  
        fname = QFileDialog.getSaveFileName(self)
        if fname[0] :
            self.save_file(fname[0])
      

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()