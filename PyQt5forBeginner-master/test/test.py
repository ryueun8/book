import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("untitled.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #test

        self.stn_1.clicked.connect(self.button1Function)
        self.stn_2.clicked.connect(self.button2Function)
        self.stn_3.clicked.connect(self.button3Function)
        self.stn_4.clicked.connect(self.button4Function)
        self.stn_5.clicked.connect(self.button5Function)
        self.stn_6.clicked.connect(self.button6Function)
        self.stn_7.clicked.connect(self.button7Function)
        self.stn_8.clicked.connect(self.button8Function)
        self.stn_9.clicked.connect(self.button9Function)

    def button1Function(self) :
        print("1번 버튼")

    def button2Function(self) :
        print("2번 버튼")

    def button3Function(self):
        print("3번 버튼")

    def button4Function(self):
        print("4번 버튼")

    def button5Function(self) :
        print("5번 버튼")

    def button6Function(self):
         print("6번 버튼")

    def button7Function(self) :
        print("7번 버튼")

    def button8Function(self):
        print("8번 버튼")

    def button9Function(self):
        print("9번 버튼")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()