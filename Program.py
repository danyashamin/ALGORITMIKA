from PyQt5.QtWidgets import QWidget, QApplication
import sys

if __name__ == '__main__':
    app_1 = QApplication(sys.argv)
    widget_1 = QWidget()
    widget_1.resize(300, 200)
    widget_1.move(300, 300)
    widget_1.setWindowTitle('MyWindow')
    widget_1.show()
    sys.exit(app_1.exec_())