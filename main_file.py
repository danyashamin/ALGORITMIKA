from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem
import sys

def func():
    print('Сработало')
app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(300, 300, 500, 300)
main_line = QVBoxLayout()
common_line = QHBoxLayout()
common_line.setSpacing(2)
list_w = QListWidget(w)
item = QListWidgetItem('Кнопка')
list_w.addItem(item)
list_w.itemSelectionChanged.connect(func)
main_line.addWidget(list_w)
w.setLayout(main_line)

w.show()
sys.exit(app.exec_())