from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import sys
import os

class NeedWindow(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle('ImageMaker')
        win = QWidget()
        global count_NeedWindow
        if count_NeedWindow==0:
            main_line = QVBoxLayout()
            common_line = QHBoxLayout()
            common_line.setSpacing(2)
            common_line.addStretch(1)
            line_small_widgets = QVBoxLayout()
            line_small_widgets.setSpacing(7)
            input_label = QLabel()
            input_label.setText('Введите имя фотографии:')
            line_small_widgets.addWidget(input_label, stretch=1)
            line_input = QLineEdit()
            line_small_widgets.addWidget(line_input, stretch=1)
            button_input = QPushButton('Искать изображение по названию')
            def input_reaction():
                if os.path.isfile(line_input.text()):
                    text_on_line = line_input.text()
                    global count_NeedWindow
                    count_NeedWindow+=1
                    win.hide()
                    self.hide()
                    self.__init__(text_on_line)
            button_input.clicked.connect(input_reaction)
            line_small_widgets.addWidget(button_input, stretch=1)
            line_small_widgets.addStretch(4)
            common_line.addLayout(line_small_widgets, stretch=1)
            main_line.addLayout(common_line)
        else:
            main_line = QVBoxLayout()
            common_line = QHBoxLayout()
            common_line.setSpacing(2)
            with Image.open(args[0]) as f_image:
                f_image = f_image.resize((int(f_image.size[0]/3), int(f_image.size[1]/3)))
                f_image.save(args[0][0:len(args[0])-4]+'.small.jpg')
            pix_small = QPixmap(args[0][0:len(args[0])-4]+'.small.jpg')
            pix_label = QLabel(self)
            pix_label.setPixmap(pix_small)
            common_line.addWidget(pix_label, stretch=1)
            line_for_buttons = QVBoxLayout()
            cut_or_resize = QHBoxLayout()
            cut_or_resize.setSpacing(2)
            cut = QPushButton('Обрезать')
            cut_or_resize.addWidget(cut, stretch=1|2)
            resize = QPushButton('Изменить размер')
            cut_or_resize.addWidget(resize, stretch=1|2)
            line_for_buttons.addLayout(cut_or_resize)
            convert_or_contrast = QHBoxLayout()
            convert_or_contrast.setSpacing(2)
            convert = QPushButton('Сделать чёрно белым')
            convert_or_contrast.addWidget(convert, stretch=1|2)
            contrast = QPushButton('Сделать контрастным')
            convert_or_contrast.addWidget(contrast, stretch=1|2)
            line_for_buttons.addLayout(convert_or_contrast)
            common_line.addLayout(line_for_buttons, stretch=1)
            main_line.addLayout(common_line)
        win.setLayout(main_line)
        self.setCentralWidget(win)
        self.show()
        global count_App
        if count_App==0:
            count_App+=1
            sys.exit(app.exec_())
app = QApplication(sys.argv)
count_NeedWindow = 0
count_App = 0

n = NeedWindow()