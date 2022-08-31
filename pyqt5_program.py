from PyQt5.QtWidgets import QApplication, QWidget
import sys

applicationOne = QApplication(sys.argv)
widgetOne = QWidget()
widgetOne.resize(500, 300)
widgetOne.move(300, 300)
widgetOne.setWindowTitle('MyLovelyWidget')
if __name__ == '__main__':
    widgetOne.show()
    sys.argv(applicationOne.exec_())