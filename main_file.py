from PIL import Image, ImageEnhance
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QInputDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class ImageEditor():
    def __init__(self, name):
        self.name = name
        self.open_image()
        print('ImageEditor')
        #self.changed_list = [self.file_original]
    def open_image(self):
        try:
            with Image.open(self.name) as file_original:
                self.file_original = file_original
                pass
        except:
            pass

class NeedApplication(QMainWindow):
    def __init__(self, *cur_app):
        super().__init__()
        self.setWindowTitle('Главное окно')
        self.work_win = QWidget()
        #create work win
        self.resize(1000, 500)
        self.main_line = QVBoxLayout()
        self.common_line = QHBoxLayout()
        self.common_line.setSpacing(2)
        # stretch for image and line with buttons
        if count_image == 0:
            #if fun work first time or if user want change image
            self.common_line.addStretch(1)
            #add stretch on place image

            #add line
            self.start_line = QVBoxLayout()
            self.start_line.setSpacing(7)
            #set spacing for normal form

            #add request label
            self.input_label = QLabel(self.work_win)
            self.input_label.setText('Введите имя изображения:')
            self.start_line.addWidget(self.input_label, stretch=1)
            
            #add line edit and prompt on it
            self.edit_line = QLineEdit()
            self.edit_line.setPlaceholderText('Введите имя')
            
            #add it on start line and signal of input button
            self.start_line.addWidget(self.edit_line, stretch=1)
            self.input_button = QPushButton('Ввёл')
            self.input_button.clicked.connect(self.click_reaction)
            self.layout_button = QHBoxLayout()
            #add it on line for good looks 
            self.layout_button.setSpacing(3)
            self.layout_button.addWidget(self.input_button, stretch=1|3, alignment=Qt.AlignCenter)

            #add button line on main line
            self.start_line.addLayout(self.layout_button, stretch=1|3)

            #fill empty space on line
            self.start_line.addStretch(4)
            self.common_line.addLayout(self.start_line, stretch=1)
        else:
            #if user choose image

            #create PIL object Image
            self.object_image = Image.open(self.edit_line.text())

            #do it convenient for user
            self.object_small = self.object_image.resize((int(self.object_image.size[0]/1.5), int(self.object_image.size[1]/1.5)))
            self.object_small.save(self.edit_line.text()[0:len(self.edit_line.text())-4]+'.small.jpg')

            #add it on common line
            self.pix_user = QPixmap(self.edit_line.text()[0:len(self.edit_line.text())-4]+'.small.jpg')
            self.label_image = QLabel(self.work_win)
            self.label_image.setPixmap(self.pix_user)
            self.common_line.addWidget(self.label_image, stretch=1)
            
            #create line for all buttons
            self.line_buttons = QVBoxLayout()

            #do line for first two buttons (with stretch between for pretty)
            self.cut_or_resize = QHBoxLayout()
            self.cut_or_resize.setSpacing(3)

            # add buttons on it
            self.cut_button = QPushButton('Обрезать')
            self.cut_button.clicked.connect(self.cut_function)
            self.cut_or_resize.addWidget(self.cut_button, stretch=1)
            self.cut_or_resize.addStretch(1)
            self.resize_button = QPushButton('Изменить размер')
            self.resize_button.clicked.connect(self.resize_function)
            self.cut_or_resize.addWidget(self.resize_button, stretch=1)

            #add line on line for all buttons
            self.line_buttons.addLayout(self.cut_or_resize)
            
            #create line for new to buttons
            self.black_or_enchance = QHBoxLayout()
            self.black_or_enchance.setSpacing(3)

            #add buttons on it
            self.black_button = QPushButton('Сделать чёрно белой')
            self.black_button.clicked.connect(self.black_fun)
            self.black_or_enchance.addWidget(self.black_button, stretch=1)
            self.black_or_enchance.addStretch(1)
            self.enchance_button = QPushButton('Сделать контрастным')
            self.enchance_button.clicked.connect(self.enchance_fun)
            self.black_or_enchance.addWidget(self.enchance_button, stretch=1)

            #add line on line for all buttons
            self.line_buttons.addLayout(self.black_or_enchance)

            #add button to change image with function for it
            self.change_button = QPushButton('Поменять изображение')
            def change_fun():
                global count_image
                #do count_image equals zero to return in start
                count_image = 0
                self.hide()
                self.__init__(app)
            self.change_button.clicked.connect(change_fun)

            #add it on common line
            self.line_buttons.addWidget(self.change_button)
            self.common_line.addLayout(self.line_buttons, stretch=1)
            #self.change_button
        #add line common line for main line
        self.main_line.addLayout(self.common_line)

        #set main line on work win
        self.work_win.setLayout(self.main_line)
        
        #set win like central widget
        self.setCentralWidget(self.work_win)
        self.show()
        global count_app
        if count_app==0:
            count_app+=1
            sys.exit(app.exec_())
    def click_reaction(self):
        self.editor = ImageEditor(self.edit_line.text())
        global count_image
        try:
            # try to add need image on line
            count_image+=1
            self.hide()
            self.__init__(app)
        except:
            #is this do imporsable, message user about it
            count_image = 0
            self.__init__()
            self.edit_line.setPlaceholderText('Изображение не найдено')
    #all the rest functions ask user about parametrs of change
    #and try to do it
    #if this is imporsable - pass
    def resize_function(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Изменение изображения', 'Введитe длину и ширину (через пробел):')
        if _:
            try:
                list_text = text.split(' ')
                print(list_text)
                new_image = self.object_image.resize((int(list_text[0]), int(list_text[1])))
                print('Изменил размер')
                d = QInputDialog()
                name, _ = d.getText(self, 'Создание изображения', 'Введите имя нового изображения:')
                new_image.save(name)
            except:
                message = QMessageBox()
                message.setText('Введите размер числами (через пробел)!')
                message.show()
                message.exec_()
    def cut_function(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Обрезание изображения', 'Введите координаты обрезаемого квадрата:')
        if _:
            try:
                list_size = text.split(' ')
                new_image = self.object_image.crop((int(list_size[0]), int(list_size[1]), int(list_size[2]), int(list_size[3])))
                d = QInputDialog()
                name, _ = d.getText(self, 'Создание изображение', 'Введите имя нового изображения')
                new_image.save(name)
            except:
                message = QMessageBox()
                message.setText('Введите координаты числами (через пробел)!')
                message.show()
                message.exec_()
    def black_fun(self):
        image_black = self.object_image.convert('L')
        d = QInputDialog()
        name, _ = d.getText(self, 'Создание изображения', 'Введите имя нового изображения:')
        image_black.save(name)
    def enchance_fun(self):
        pic_contrast = ImageEnhance.Contrast(self.object_image)
        d = QInputDialog()
        text, _ = d.getText(self, 'Изменение контраста', 'Введите нужный контраст:')
        if _:
            try:
                pic_contrast = pic_contrast.enhance(float(text))
                d = QInputDialog()
                name, _ = d.getText(self, 'Создание изображения', 'Введите имя нового изображения:')
                try:
                    if _:
                        pic_contrast.save(name)
                except:
                    message = QMessageBox()
                    message.setText('Введите осознанное имя!')
                    message.show()
                    message.exec_()
            except:
                message = QMessageBox()
                message.setText('Введите контраст числом!')
                message.show()
                message.exec_()


count_image = 0
count_app = 0
app = QApplication(sys.argv)
i = NeedApplication(app)
#создай объект класса ImageEditor с данными картинки-оригинала

#отредактируй изображение и сохрани результат
