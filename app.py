import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon

form_class = uic.loadUiType("./sungha.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setWindowTitle("test")
        self.setWindowIcon(QIcon('web.png')) #여기에 main icon 부착
        self.pushButton.clicked.connect(self.btnClick)
        self.pushButton_2.clicked.connect(self.btnClick2)
        self.pushButton_3.clicked.connect(self.btnClick3)
        self.pushButton_4.clicked.connect(self.btnClick4)
        self.pushButton_5.clicked.connect(self.btnClick5)

    def btnClick(self):
        print("버튼이 클릭되었습니다.")
    def btnClick2(self):
        print("두번째 버튼이 클릭되었습니다.")
    def btnClick3(self):
        print("세번째 버튼이 클릭되었습니다.")
    def btnClick4(self):
        print("네번째 버튼이 클릭되었습니다.")
    def btnClick5(self):
        print("다섯번째 버튼이 클릭되었습니다.")


if __name__ == "__main__":
    app = QApplication(sys.argv) #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야한다.
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()