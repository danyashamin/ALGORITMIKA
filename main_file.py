from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    win.setGeometry(300, 300, 500, 300)
    main_line = QVBoxLayout()
    common_line = QHBoxLayout()
    common_line.setSpacing(2)
    list_w = QListWidget()
    common_line.addWidget(list_w, stretch=1)
    small_widgets_line = QVBoxLayout()
    small_widgets_line.setSpacing(2)
    first_half = QVBoxLayout()
    caption_list_zametks = QLabel(win)
    caption_list_zametks.setText('Список заметок')
    first_half.addWidget(caption_list_zametks)
    list_zametks = QListWidget()
    first_half.addWidget(list_zametks)
    buttons_zametks_line = QHBoxLayout()
    buttons_zametks_line.setSpacing(2)
    button_1 = QPushButton('Кнопка 1')
    buttons_zametks_line.addWidget(button_1)
    button_2 = QPushButton('Кнопка 2')
    buttons_zametks_line.addWidget(button_2)
    first_half.addLayout(buttons_zametks_line)
    button_big_1 = QPushButton('Кнопка бльшая 1')
    first_half.addWidget(button_big_1)
    small_widgets_line.addLayout(first_half, stretch=1|2)
    
    first_half = QVBoxLayout()
    caption_list_zametks = QLabel(win)
    caption_list_zametks.setText('Список тегов')
    first_half.addWidget(caption_list_zametks)
    list_zametks = QListWidget()
    first_half.addWidget(list_zametks)
    buttons_zametks_line = QHBoxLayout()
    buttons_zametks_line.setSpacing(2)
    button_1 = QPushButton('Кнопка 1_2')
    buttons_zametks_line.addWidget(button_1)
    button_2 = QPushButton('Кнопка 2_2')
    buttons_zametks_line.addWidget(button_2)
    first_half.addLayout(buttons_zametks_line)
    button_big_1 = QPushButton('Кнопка бльшая 2')
    first_half.addWidget(button_big_1)
    small_widgets_line.addLayout(first_half, stretch=1|2)

    common_line.addLayout(small_widgets_line, stretch=1)
    main_line.addLayout(common_line)

    win.setLayout(main_line)
    win.show()
    sys.exit(app.exec_())