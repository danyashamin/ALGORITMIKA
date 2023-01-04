from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
import sys

class NeedWindow(QMainWindow):
    def __init__(self, *args):
        #def common_fun():
        super().__init__()
        self.setWindowTitle('Моё окно')
        self.setGeometry(200, 100, 1000, 600)
        self.win_main = QWidget()
        self.main_line = QVBoxLayout()
        self.HLine = QHBoxLayout()
        self.HLine.setSpacing(2)
        if len(args)>0:
            with Image.open(args[0]) as image_cur:
                image_cur = image_cur.resize((500, 500))
                image_cur.save(args[0][0:9]+'.small.jpg')
            self.pix_cur = QPixmap(args[0][0:9]+'.small.jpg')
            self.label_image = QLabel(self)
            self.label_image.setPixmap(self.pix_cur)
            self.HLine.addWidget(self.label_image, stretch=1)
        else:
            self.HLine.addStretch(1)
            self.VLine = QVBoxLayout()
            self.VLine.setSpacing(8)
            self.input_label = QLabel(self)
            self.input_label.setText('Введите имя изображения                                                   ')
            self.VLine.addWidget(self.input_label)
            self.input_line = QLineEdit()
            self.input_line.setPlaceholderText('Введите место сущестующего изображения')
            self.VLine.addWidget(self.input_line)
            self.input_button = QPushButton('Ввёл')
            self.input_button.clicked.connect(self.input_reaction)
            self.VLine.addWidget(self.input_button)
            self.VLine.addStretch(5)
            self.HLine.addLayout(self.VLine)

        self.main_line.addLayout(self.HLine)
        self.win_main.setLayout(self.main_line)
        
        self.setCentralWidget(self.win_main)
        self.show()
        global count_cycle
        if count_cycle==0:
            count_cycle+=1
            sys.exit(app.exec_())
    def input_reaction(self):
        try:
            self.close()
            self.__init__(self.input_line.text())
        except:
            pass

#global constants
count_cycle = 0

app = QApplication(sys.argv)
n = NeedWindow()