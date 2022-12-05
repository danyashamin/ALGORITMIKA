import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt
import sys

class NeedWind(QWidget):
    def __init__(self):
        global count
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Memory Card')
        
        self.common_line = QVBoxLayout()
        self.line_h = QHBoxLayout()
        self.line_h.addStretch(1)
        self.edit_big = QTextEdit()
        self.edit_big_line = QVBoxLayout()
        self.edit_big_line.addWidget(self.edit_big, stretch=1)
        self.line_h.addLayout(self.edit_big_line)

        self.small_widgets_line = QVBoxLayout()
        self.small_widgets_line.addStretch(3)
        self.edit_small = QTextEdit()
        self.small_widgets_line.addWidget(self.edit_small, stretch=1)
        self.line_h.addLayout(self.small_widgets_line)

        self.common_line.addLayout(self.line_h)

        self.setLayout(self.common_line)

        self.show()
        if count == 0:
            count+=1
            sys.exit(app.exec_())

with open('file_my.json') as file_my:
    dict_my = json.load(file_my)
    print(dict_my)

app = QApplication(sys.argv)
count = 0
n = NeedWind()