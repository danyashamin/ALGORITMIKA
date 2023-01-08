from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout
import sys

class MyWind(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.main_line = QVBoxLayout()
        self.button_line = QHBoxLayout()
        self.button_line.setSpacing(5)
        self.button_line.addStretch(2)
        self.button_1 = QPushButton('Кнопка_1')
        self.button_1.clicked.connect(self.func_1)
        self.button_line.addWidget(self.button_1, stretch=1)
        self.button_line.addStretch(2)
        self.main_line.addLayout(self.button_line)
        self.setLayout(self.main_line)


        self.show()
        global count_app
        print(count_app)
        if count_app>0:
            win_2 = QWidget()
            win_2.setGeometry(200, 200, 300, 300)
            win_2.show()
        if count_app==0:
            count_app+=1
            sys.exit(app.exec_())
    def func_1(self):
        global count_app
        count_app+=1
        self.__init__()

app = QApplication(sys.argv)
count_app = 0
m = MyWind()