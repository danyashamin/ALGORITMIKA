from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class NeedWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 1000, 500)
        
        self.show()
        sys.exit(app.exec_())
app = QApplication(sys.argv)
w = NeedWin()