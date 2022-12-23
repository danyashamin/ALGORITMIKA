from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QTextEdit, QPushButton, QLineEdit, QInputDialog
import sys
import json

class NeedWindow(QWidget):
    def __init__(self):
        global count
        super().__init__()
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Нужное окно')
        self.main_line = QVBoxLayout()
        self.common_line = QHBoxLayout()
        self.common_line.setSpacing(2)
        self.big_edit = QTextEdit()
        self.common_line.addWidget(self.big_edit, stretch=1|2)
        self.small_edits_line = QVBoxLayout()
        self.small_edits_line.setSpacing(2)
        self.line_first = QVBoxLayout()
        self.list_zametks_label = QLabel(self)
        self.list_zametks_label.setText('Список заметок')
        self.line_first.addWidget(self.list_zametks_label)
        self.list_zametks = QListWidget()
        if count==0:
            self.list_zametks.addItem('Добро пожаловать!')
            self.list_zametks.itemSelectionChanged.connect(self.dobro_pozhalovat)
        else:
            for zametka, teg in zip(dict_cur.keys(), dict_cur.values()):
                self.list_zametks.addItem(zametka)
                def fun_cur():
                    self.big_edit.setText(teg[1])
                self.list_zametks.itemSelectionChanged.connect(fun_cur)
        self.line_first.addWidget(self.list_zametks)
        self.line_buttons_1 = QHBoxLayout()
        self.line_buttons_1.setSpacing(2)
        self.create_zametka_button = QPushButton('Создать заметку')
        self.create_zametka_button.clicked.connect(self.create_zametka_fun)
        self.line_buttons_1.addWidget(self.create_zametka_button, stretch=1|2)
        self.delete_zametka_button = QPushButton('Удалить заметку')
        self.line_buttons_1.addWidget(self.delete_zametka_button, stretch=1|2)
        self.line_first.addLayout(self.line_buttons_1, stretch=1|2)
        self.save_zametka = QPushButton('Сохранить заметку')
        self.line_first.addWidget(self.save_zametka)

        self.line_second = QVBoxLayout()
        self.list_tegs_label = QLabel(self)
        self.list_tegs_label.setText('Список тегов')
        self.line_second.addWidget(self.list_tegs_label)
        self.list_tegs = QListWidget()
        if count!=0:
            print('Зашёл в теги')
            for zametka, teg in zip(dict_cur.keys(), dict_cur.values()):
                self.list_tegs.addItem(teg[0])
                def fun_cur():
                    self.big_edit.setText(teg[1])
                self.list_tegs.itemSelectionChanged.connect(fun_cur)
        self.line_second.addWidget(self.list_tegs)
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText('Введите тег')
        self.line_second.addWidget(self.input_line)
        self.line_buttons_2 = QHBoxLayout()
        self.line_buttons_2.setSpacing(2)
        self.add_teg_to_zametks = QPushButton('Добавить к заметкам')
        self.add_teg_to_zametks.clicked.connect(self.add_to_zametks_fun)
        self.line_buttons_2.addWidget(self.add_teg_to_zametks, stretch=1|2)
        self.delete_from_zametks = QPushButton('Открепить от заметок')
        self.line_buttons_2.addWidget(self.delete_from_zametks, stretch=1|2)
        self.line_second.addLayout(self.line_buttons_2)
        self.find_zametks_by_teg = QPushButton('Искать заметки по тегу')
        self.find_zametks_by_teg.clicked.connect(self.find_zametka_by_teg_fun)
        self.line_second.addWidget(self.find_zametks_by_teg)
        
        self.small_edits_line.addLayout(self.line_first, stretch=1|2)
        self.small_edits_line.addLayout(self.line_second, stretch=1|2)
        self.common_line.addLayout(self.small_edits_line, stretch=1|2)
        self.main_line.addLayout(self.common_line)
        self.setLayout(self.main_line)
        self.show()
        if count==0:
            count+=1
            sys.exit(app.exec_())
    def dobro_pozhalovat(self):
        global count
        count+=1
        self.hide()
        self.__init__()
    def create_zametka_fun(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Создание заметки', 'Введите заметку:')
        if _:
            self.hide()
            dict_cur[text] = ['', '']
            self.__init__()
    def del_zametka_fun(self):
        d = QInputDialog()
        text, _ = d.getText(self, 'Удаление заметки', 'Введите заметку')
        if _:
            self.hide()
            dict_cur.pop(text)
            self.__init__()
    def add_to_zametks_fun(self):
        self.hide()
        for zametka, teg in zip(dict_cur.keys(), dict_cur.values()):
            print('Ищу')
            print(zametka, teg)
            if teg == ['', '']:
                print('Попал')
                dict_cur[zametka] == [self.input_line.text(), self.big_edit.toPlainText()]
        self.__init__()
    def find_zametka_by_teg_fun(self):
        for zametka, teg in zip(dict_cur.keys(), dict_cur.values()):
            print(teg[0], self.input_line.text())
            if teg[0]==self.input_line.text():
                self.big_edit.setText(teg[1])
                print('Нашёл')
        print('Я здесь')
        self.show()
    def save_zametka_fun(self):
        with open('file_j.json') as f_save:
            f_cur = json.dump(f_save, dict_cur)
            f_save.close()

with open('file_j.json') as f_cur:
    dict_cur = json.load(f_cur)
    print(dict_cur)
    f_cur.close()

app = QApplication(sys.argv)
count = 0

n = NeedWindow()