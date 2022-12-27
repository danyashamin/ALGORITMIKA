from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(300, 300, 1000, 500)
label = QLabel(win)
label.setText('Лабель')
label.move(700, 400)
win.show()
sys.exit(app.exec_())