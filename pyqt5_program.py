from PyQt5.QtWidgets import QApplication, QWidget
import sys

f_program_name = sys.argv[0]
f_program = open(f_program_name, 'br')
print(f_program.read()[0])
if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(250, 150)
    widget.move(100, 100)
    widget.setWindowTitle('Window')
    widget.show()
    sys.exit(app.exec_())
    