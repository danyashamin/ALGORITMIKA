from PyQt5.QtWidgets import QApplication, QWidget
import sys

print(sys.argv)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget_1 = QWidget()
    widget_1.resize(250, 150)
    widget_1.move(300, 300)
    widget_1.setWindowTitle("Title")
    widget_1.show()
    sys.exit(app.exec_())