from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QInputDialog
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
                image_cur.save(args[0][0:len(args)-5]+'.small.jpg')
            self.pix_cur = QPixmap(args[0][0:len(args)-5]+'.small.jpg')
            self.label_image = QLabel(self)
            self.label_image.setPixmap(self.pix_cur)
            self.HLine.addWidget(self.label_image, stretch=1)
            self.buttons_line = QVBoxLayout()
            self.resize_or_cut = QHBoxLayout()
            self.buttons_line.setSpacing(2)
            self.resize_image = QPushButton('Поменять размер')
            self.resize_image.clicked.connect(self.change_size)
            self.resize_or_cut.addWidget(self.resize_image, stretch=1)
            #self.resize_or_cut.addStretch(1)
            self.cut_image = QPushButton('Обрезать')
            self.resize_or_cut.addWidget(self.cut_image, stretch=1)
            self.buttons_line.addLayout(self.resize_or_cut)
            self.black_or_endhance = QHBoxLayout()
            self.black_or_endhance.setSpacing(2)
            self.black = QPushButton('Сделать чёрно-белым')
            self.black_or_endhance.addWidget(self.black, stretch=1)
            #self.black_or_endhance.addStretch(1)
            self.enchance = QPushButton('Сделать что-то непонятное')
            self.black_or_endhance.addWidget(self.enchance, stretch=1)
            self.buttons_line.addLayout(self.black_or_endhance)
            self.HLine.addLayout(self.buttons_line)
        else:
            self.HLine.addStretch(1)
            self.VLine = QVBoxLayout()
            self.VLine.setSpacing(8)
            self.input_label = QLabel(self)
            self.input_label.setText('Введите имя изображения')
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
            self.input_line.setPlaceholderText('Нет такой директории')
    def change_size(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Изменение размера', 'Введите нужный размер:')
        if _:
            #try:
                list_size = text.split(' ')
                global image_cur
                image_cur = image_cur.resize(list_size[0], list_size[1])
                d = QInputDialog()
                text, _ = d.getText(self, 'Создание изображение', 'Введите название изображения:')
                image_cur.save(text)
            #except:
            #    pass


#global constants
count_cycle = 0

app = QApplication(sys.argv)
n = NeedWindow()