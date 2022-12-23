from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QTextEdit, QPushButton, QLineEdit
import sys

class NeedWindow(QWidget):
    def __init__(self):
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
        self.line_first.addWidget(self.list_zametks)
        self.line_buttons_1 = QHBoxLayout()
        self.line_buttons_1.setSpacing(2)
        self.create_zametka_button = QPushButton('Создать заметку')
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
        self.line_second.addWidget(self.list_tegs)
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText('Введите тег')
        self.line_buttons_2 = QHBoxLayout()
        self.line_buttons_2.setSpacing(2)
        self.add_teg_to_zametks = QPushButton('Добавить к заметкам')
        self.line_buttons_2.addWidget(self.add_teg_to_zametks, stretch=1|2)
        self.delete_from_zametks = QPushButton('Открепить от заметок')
        self.line_buttons_2.addWidget(self.delete_from_zametks, stretch=1|2)
        self.line_second.addLayout(self.line_buttons_2)
        self.find_zametks_by_teg = QPushButton('Искать заметки по тегу')
        self.line_second.addWidget(self.find_zametks_by_teg)
        
        self.small_edits_line.addLayout(self.line_first, stretch=1|2)
        self.small_edits_line.addLayout(self.line_second, stretch=1|2)
        self.common_line.addLayout(self.small_edits_line, stretch=1|2)
        self.main_line.addLayout(self.common_line)
        self.setLayout(self.main_line)
        self.show()
        global count
        if count==0:
            count+=1
            sys.exit(app.exec_())

app = QApplication(sys.argv)
count = 0

n = NeedWindow()