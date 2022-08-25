from PyQt5.QtWidgets import QApplication, QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget_1 = QWidget()
    widget_1.resize(500, 300)
    widget_1.setWindowTitle('Открылось окно, закрой')
    widget_1.move(300, 300)
    widget_1.show()
    sys.exit(app.exec_())