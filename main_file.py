from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QInputDialog, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt
import sys
import json

class NeedWindow(QWidget):
    def __init__(self):
        global count_cycle
        super().__init__()
        self.setWindowTitle('Memory Card')
        self.setGeometry(100, 100, 900, 600)
        self.common_line = QHBoxLayout()
        self.common_line.setSpacing(3)
        self.big_edit = QTextEdit()
        self.common_line.addWidget(self.big_edit, stretch=2)

        self.small_widgets_line = QVBoxLayout()
        self.label_zametks = QLabel(self)
        self.label_zametks.setText('Список заметок')
        self.small_widgets_line.addWidget(self.label_zametks)
        self.zametks_list = QListWidget()
        if count_cycle==0:
            self.zametks_list.addItem('Добро пожаловать!')
            self.zametks_list.itemSelectionChanged.connect(self.hello_world)
        else:
            for zametka, teg in zip(f_dict.keys(), f_dict.values()):
                self.zametks_list.addItem(zametka)
                def func_cur():
                    self.big_edit.setText(teg[1])
                self.zametks_list.itemSelectionChanged.connect(func_cur)
        self.small_widgets_line.addWidget(self.zametks_list)
        self.zametks_buttons_line = QHBoxLayout()
        self.zametks_buttons_line.setSpacing(2)
        self.create_zametka = QPushButton('Создать заметку')
        self.create_zametka.clicked.connect(self.create_zametka_fun)
        self.zametks_buttons_line.addWidget(self.create_zametka, stretch=1)
        self.delete_zametka = QPushButton('Удалить заметку')
        self.delete_zametka.clicked.connect(self.delete_zametka_fun)
        self.zametks_buttons_line.addWidget(self.delete_zametka, stretch=1)
        self.small_widgets_line.addLayout(self.zametks_buttons_line)
        self.save_zametka = QPushButton('Сохранить заметку')
        self.save_zametka.clicked.connect(self.save_zametka_fun)
        self.small_widgets_line.addWidget(self.save_zametka)
        self.small_widgets_line.addStretch(1)

        self.label_tegs = QLabel(self)
        self.label_tegs.setText('Список тегов')
        self.small_widgets_line.addWidget(self.label_tegs)
        self.tegs_list = QListWidget()
        for key, value in zip(f_dict.keys(), f_dict.values()):
            self.tegs_list.addItem(value[0])
        self.small_widgets_line.addWidget(self.tegs_list)
        self.line_input_teg = QLineEdit()
        self.line_input_teg.setPlaceholderText('Введите тег')
        self.small_widgets_line.addWidget(self.line_input_teg)
        self.tegs_buttons_line = QHBoxLayout()
        self.tegs_buttons_line.setSpacing(2)
        self.add_to_zametks = QPushButton('Добавить к заметкам')
        self.add_to_zametks.clicked.connect(self.add_teg_fun)
        self.tegs_buttons_line.addWidget(self.add_to_zametks, stretch=1)
        self.delete_from_zametks = QPushButton('Открепить от заметок')
        self.delete_from_zametks.clicked.connect(self.del_teg_fun)
        self.tegs_buttons_line.addWidget(self.delete_from_zametks, stretch=1)
        self.small_widgets_line.addLayout(self.tegs_buttons_line)
        self.find_zametks_by_teg = QPushButton('Искать заметки по тегу')
        self.find_zametks_by_teg.clicked.connect(self.find_zametks_by_teg_fun)
        self.small_widgets_line.addWidget(self.find_zametks_by_teg)
        self.common_line.addLayout(self.small_widgets_line, stretch=1)

        self.main_line = QVBoxLayout()
        self.main_line.addLayout(self.common_line)
        self.setLayout(self.main_line)

        self.show()
        if count_cycle==0:
            count_cycle+=1
            sys.exit(app.exec_())
    def hello_world(self):
        self.hide()
        self.__init__()
    def create_zametka_fun(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Создание заметки', 'Введите заметку:')

        if _:
            self.hide()
            f_dict[text] = [self.line_input_teg.text(), self.big_edit.toPlainText()]
            self.__init__()
    def save_zametka_fun(self):
        with open('file_j.json', 'w', encoding="UTF-8") as f_cur:
            json.dump(f_dict, f_cur)
            f_cur.close()
            self.hide()
            self.__init__()
    def delete_zametka_fun(self):
        d = QInputDialog()
        text, _ = d.getText(self, "Удаление заметки", "Введите заметку:")
        if _:
            self.close()
            if text in f_dict:
                f_dict.pop(text)
            self.__init__()
    def add_teg_fun(self):
        for key, value in zip(f_dict.keys(), f_dict.values()):
            if value == ['','']:
                f_dict[key] = [self.line_input_teg.text(), self.big_edit.toPlainText()]
        self.close()
        self.__init__()
    def del_teg_fun(self):
        for key, value in zip(f_dict.keys(), f_dict.values()):
            if value[0] == self.line_input_teg.text():
                f_dict[key] = ['', '']
        self.close()
        self.__init__()
    def find_zametks_by_teg_fun(self):
        for zametka, teg in zip(f_dict.keys(), f_dict.values()):
            if teg[0] == self.line_input_teg.text():
                self.big_edit.setText(teg[1])
        self.show()

with open('file_j.json', 'r', encoding="UTF-8") as f_cur:
    f_dict = json.load(f_cur)
    f_cur.close()

count_cycle = 0
app = QApplication(sys.argv)
w= NeedWindow()