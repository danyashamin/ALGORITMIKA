from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QVBoxLayout, QHBoxLayout, QTextEdit
import sys

class NeedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 1200, 600)
        self.main_line = QVBoxLayout()
        self.common_line = QHBoxLayout()
        self.big_edit = QListWidget()
        self.common_line.setSpacing(2)
        self.common_line.addWidget(self.big_edit, stretch=1)
        self.small_edits_line = QVBoxLayout()
        self.small_edits_line.addWidget(QLabel(self).setText('Список заметок:'))
        self.common_line.addLayout(self.small_edits_line, stretch=1)
        self.main_line.addLayout(self.common_line)
        self.setLayout(self.main_line)
        self.show()
        global count
        if count == 0:
            count+=1
            sys.exit(app.exec_())

count = 0
app = QApplication(sys.argv)
n = NeedWindow()