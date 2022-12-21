from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
 
import json
import os.path

# Создали файл если его не было
if not os.path.exists("notes_data.json"):
    with open("notes_data.json", "w") as file:
        json.dump({}, file)
 
app = QApplication([])

'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)
 
#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
 
button_note_create = QPushButton('Создать заметку') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
 
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
 
#расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
 
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
 
col_2.addLayout(row_3)
col_2.addLayout(row_4)
 
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
 
'''Функционал приложения'''
def show_note():
    #получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

def create_note():
    text, ok = QInputDialog().getText(None, 'Ввод', 'Введите название заметки')
    if ok == True and text != '' and text not in notes:
        notes[text] = {'теги': [], 'текст': ''}
        list_notes.clear()
        list_notes.addItems(notes)
    elif text in notes:
        print('Заметка с таким именем уже есть!')
    elif text == '':
        print('Название заметки не может быть пустым!')

def save_notes():
    with open("notes_data.json", "w") as file:
        json.dump(notes, file)

def add_tag():
    selected = list_notes.selectedItems()
    if len(selected) == 0:
        print('Выбери заметку!')
    else:
        note = selected[0].text()
        text, ok = QInputDialog().getText(None, 'Ввод', 'Введите название тега')
        if ok == True and text != '' and text not in notes[note]['теги']:
            notes[note]['теги'].append(text)
            list_tags.clear()
            list_tags.addItems(notes[note]['теги'])
        elif text in notes[note]['теги']:
            print('Такой тег уже привязан к заметке')
        elif text == '':
            print('Тег не может быть пустым!')

def search():
    res = []
    text = field_tag.text()
    if text == '':
        print('Введите текст')
    else:
        for note in notes:
            if text in notes[note]['теги']:
                res.append(note)
    list_notes.clear()
    list_notes.addItems(res)

'''Запуск приложения'''
#подключение обработки событий
list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(create_note)
button_note_save.clicked.connect(save_notes)
button_tag_add.clicked.connect(add_tag)
button_tag_search.clicked.connect(search)
 
#запуск приложения
notes_win.show()
 
with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
 
app.exec_()