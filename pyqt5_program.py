from PyQt5.QtWidgets import QApplication, QWidget
import sys

f_program_name = sys.argv[0]
file_program = open(f_program_name, 'br')
print(file_program.read()[0])

if __name__ == '__main__':
    print(sys.argv)
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(800, 600)
    widget.move(150, 150)
    widget.setWindowTitle('Title')
    widget.setObjectName('form')
    widget.show()
    sys.exit(app.exec_())