from email.mime import application
from PyQt5.QtWidgets import QApplication, QWidget
import sys

applicationOne = QApplication(sys.argv)
widgetOne = QWidget()
widgetOne.resize(500, 300)
widgetOne.move(300, 300)
widgetOne.setWindowTitle('MyLovelyWidget')
applicationTwo = QApplication(sys.argv)
widgetTwo = QWidget()
widgetTwo.resize(500, 300)
widgetTwo.move(800, 300)
widgetTwo.setWindowTitle('MyNotLovelyWidget')
if __name__ == '__main__':
    widgetOne.show()
    widgetTwo.show()
    sys.argv(applicationOne.exec_())