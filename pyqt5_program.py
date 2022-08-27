from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
widget_1 = QWidget()
widget_1.resize(500, 300)
widget_1.move(400, 600)
widget_1.setWindowTitle('Окно')
if __name__ == '__main__':
    widget_1.show()
    sys.exit(app.exec_())