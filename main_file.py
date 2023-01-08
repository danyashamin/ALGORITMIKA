from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
import os
import sys

class NeedWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle('Лучшее приложение в мире')
        self.setGeometry(300, 300, 1000, 500)
        self.main_line = QVBoxLayout()
        self.main_line.setSpacing(3)
        self.common_line = QHBoxLayout()
        self.common_line.setSpacing(2)
        self.label_image = QLabel(self)
        self.pix_image = QPixmap(name)
        self.pix_on_screen = Image.open(name)
        self.pix_on_screen = self.pix_on_screen.resize((int(self.pix_on_screen.size[0]/3), int(self.pix_on_screen.size[1]/3)))
        self.pix_on_screen.save(name[0:len(name)-4]+'screen.jpg')
        self.pix_on_screen = QPixmap(name[0:len(name)-4]+'screen.jpg')
        self.label_image.setPixmap(self.pix_on_screen)
        self.common_line.addWidget(self.label_image, stretch=1)
        self.buttons_line = QVBoxLayout()
        self.buttons_line.setSpacing(3)
        self.cut_or_resize = QHBoxLayout()
        self.cut_or_resize.setSpacing(3)
        self.cut_button = QPushButton('Обрезать')
        self.cut_or_resize.addWidget(self.cut_button, stretch=1)
        self.cut_or_resize.addStretch(1)
        self.resize_button = QPushButton('Изменить размер')
        self.cut_or_resize.addWidget(self.resize_button, stretch=1)
        self.buttons_line.addLayout(self.cut_or_resize)
        self.convert_or_contrast = QHBoxLayout()
        self.convert_or_contrast.setSpacing(3)
        self.convert_button = QPushButton('Сделать чёрно-белым')
        self.convert_or_contrast.addWidget(self.convert_button, stretch=1)
        self.convert_or_contrast.addStretch(1)
        self.contrast_button = QPushButton('Увеличить контраст')
        self.convert_or_contrast.addWidget(self.contrast_button, stretch=1)
        self.buttons_line.addLayout(self.convert_or_contrast)
        self.save_line = QHBoxLayout()
        self.save_line.setSpacing(3)
        self.save_button = QPushButton('Сохранить')
        self.save_line.addWidget(self.save_button, stretch=1)
        self.buttons_line.addLayout(self.save_line)
        self.common_line.addLayout(self.buttons_line, stretch=1)
        self.main_line.addLayout(self.common_line)
        self.help_win = QWidget()
        self.help_win.setLayout(self.main_line)
        self.setCentralWidget(self.help_win)
        self.show()

def image_work_win():
    def start():
        print(os.path.isfile(line_input.text()))
        if os.path.isfile(line_input.text()):
            print('Условие выполнилось')
            nonlocal question_win
            question_win.hide()
            question_win = NeedWindow(line_input.text())
    question_win = QMainWindow()
    question_win.setWindowTitle('Приложение для обработки фото')
    question_win.setGeometry(300, 300, 1000, 500)
    main_line = QVBoxLayout()
    main_line.setSpacing(5)
    question = QLabel(question_win)
    question.setText('Введите имя изображения:')
    main_line.addWidget(question, alignment=Qt.AlignCenter, stretch=1)
    main_line.addStretch(1)
    line_input = QLineEdit()
    main_line.addWidget(line_input, stretch=1)
    main_line.addStretch(1)
    button_line = QHBoxLayout()
    button_line.setSpacing(5)
    button_line.addStretch(2)
    button_start = QPushButton('Нажмите чтобы начать')
    button_start.clicked.connect(start)
    button_line.addWidget(button_start, stretch=1)
    button_line.addStretch(2)    
    main_line.addLayout(button_line)
    main_line.addStretch(2)
    help_win = QWidget()
    help_win.setLayout(main_line)
    question_win.setCentralWidget(help_win)
    question_win.show()
    sys.exit(app.exec_())

count_win = 0
app = QApplication(sys.argv)


image_work_win()