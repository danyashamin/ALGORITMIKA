from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
import sys

if __name__ == '__main__':
    application_1 = QApplication(sys.argv)
    widget_1 = QWidget()
    widget_1.resize(500, 400)
    widget_1.move(300, 300)
    widget_1.setWindowTitle('My_title')
    widget_1.show()
    sys.argv(application_1.exec_())
