import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic

form_class = uic.loadUiType("untitled1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.groupBox_rbtn_1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_3.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_4.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_5.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_6.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_7.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_8.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rbtn_9.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self) :
        if self.groupBox_rbtn_1.isChecked() : print("GroupBox_rad1 Chekced")
        elif self.groupBox_rbtn_2.isChecked() : print("GroupBox_rad2 Checked")
        elif self.groupBox_rbtn_3.isChecked() : print("GroupBox_rad3 Checked")
        elif self.groupBox_rbtn_4.isChecked() : print("GroupBox_rad4 Checked")
        elif self.groupBox_rbtn_5.isChecked() : print("GroupBox_rad4 Checked")
        elif self.groupBox_rbtn_6.isChecked() : print("GroupBox_rad4 Checked")
        elif self.groupBox_rbtn_7.isChecked() : print("GroupBox_rad4 Checked")
        elif self.groupBox_rbtn_8.isChecked() : print("GroupBox_rad4 Checked")
        elif self.groupBox_rbtn_9.isChecked() : print("GroupBox_rad4 Checked")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
