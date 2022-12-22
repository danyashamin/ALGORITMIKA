from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class StartWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 500)
        self.show()
        print(Qt.AlignLeft)
        global count_cycle
        if count_cycle==0:
            count_cycle+=1
            sys.exit(app.exec_())

app = QApplication(sys.argv)
count_cycle = 0
w = StartWin()