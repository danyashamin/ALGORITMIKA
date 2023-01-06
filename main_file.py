from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import sys

class NeedWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.setGeometry(300, 300, 1000, 500)
        self.main_line = QVBoxLayout()
        self.common_line = QHBoxLayout()
        self.common_line.setSpacing(2)
        self.label_image = QLabel(self)
        self.pix_image = QPixmap(name)
        self.label_image.setPixmap(self.pix_image)
        self.common_line.addWidget(self.label_image)
        self.main_line.addLayout(self.common_line)
        self.help_win = QWidget()
        self.help_win.setLayout(self.main_line)
        self.setCentralWidget(self.help_win)
        self.show()

def start_win():
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


start_win()