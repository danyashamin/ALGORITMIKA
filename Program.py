from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QRadioButton, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys


class WinMy():
    def __init__(self, cur_q_number, questions, cur_cycle_number):
        self.cur_q_number = cur_q_number
        self.cur_cycle_number = cur_cycle_number
        self.questions = questions
        self.win_main = QWidget()
        self.win_main.setWindowTitle('Викторина')
        self.win_main.resize(500, 300)
        self.win_main.move(300, 300)
        self.main_line = QVBoxLayout()
        self.line_question = QHBoxLayout()
        self.question = self.questions[self.cur_q_number][0]
        self.question_l_1 = QLabel()
        self.question_l_1.setText(self.question)
        self.line_question.addWidget(self.question_l_1)
        self.answer_line_1 = QHBoxLayout()
        self.answer_1 = QRadioButton(self.questions[self.cur_q_number][1])
        self.answer_line_1.addWidget(self.answer_1, alignment=Qt.AlignLeft)
        self.answer_2 = QRadioButton(self.questions[self.cur_q_number][2])
        self.answer_line_1.addWidget(self.answer_2, alignment=Qt.AlignRight)
        self.answer_line_2 = QHBoxLayout()
        self.answer_3 = QRadioButton(self.questions[self.cur_q_number][3])
        self.answer_line_2.addWidget(self.answer_3, alignment=Qt.AlignLeft)
        self.answer_4 = QRadioButton(self.questions[self.cur_q_number][4])
        self.answer_line_2.addWidget(self.answer_4, alignment=Qt.AlignRight)
        self.answer_button = QPushButton('Ответить')
        self.answer_button.clicked.connect(self.answer_button_step)
        self.next_button = QPushButton('Следующий сопрос')
        self.next_button.clicked.connect(self.next_question_generate)
        self.common_answer_line = QVBoxLayout()
        self.common_answer_line.addLayout(self.answer_line_1)
        self.common_answer_line.addLayout(self.answer_line_2)
        self.common_answer_line.setSpacing(3)
        self.common_answer_box = QGroupBox()
        self.common_answer_box.setLayout(self.common_answer_line)
        self.main_line.addWidget(self.question_l_1, alignment=Qt.AlignCenter)
        self.main_line.addWidget(self.common_answer_box)
        self.main_line.addWidget(self.answer_button)
        self.main_line.addWidget(self.next_button)
        self.main_line.setSpacing(5)
        self.win_main.setLayout(self.main_line)
        self.win_main.show()
        if cur_cycle_number==0:
            cur_cycle_number+=1
            sys.exit(app.exec_())
    def answer_button_step(self):
        self.cur_cycle_number+=1
        message = QMessageBox()
        message.setWindowTitle('Результат')
        if (self.answer_1.isChecked() and self.questions[self.cur_q_number][5] == 1) or (self.answer_2.isChecked() and self.questions[self.cur_q_number][5] == 2) or (self.answer_3.isChecked() and self.questions[self.cur_q_number][5] == 3) or (self.answer_4.isChecked() and self.questions[self.cur_q_number][5] == 4):
            message.setText('Вы ответили правильно')
        else:
            message.setText('Вы ответили неправильно')
        message.show()
        message.exec_()
    def next_question_generate(self):
        if self.cur_q_number<len(self.questions)-1:
            self.cur_q_number+=1
            self.cur_cycle_number+=1
            self.__init__(self.cur_q_number, self.questions, self.cur_cycle_number)
        else:
            self.win_main = QWidget()
            self.win_main.move(300, 300)
            self.win_main.resize(500, 300)
            label_end = QLabel()
            label_end.setText('Все вопросы кончились!')
            common_end_line = QVBoxLayout()
            line_end = QHBoxLayout()
            line_end.addWidget(label_end, alignment=Qt.AlignCenter)
            ok_line = QHBoxLayout()
            ok_button = QPushButton('OK')
            ok_line.addWidget(ok_button)
            ok_line.setSpacing(1)
            common_end_line.addLayout(line_end)
            common_end_line.addLayout(ok_line)
            self.win_main.setLayout(common_end_line)
            self.win_main.show()

app = QApplication(sys.argv)
win_1 = WinMy(0, [['Какое самое высокое здание в мире?', 'Эйфилева башня', 'Буршхалиф', 'Пирамида Хеопса', 'Останскинская башня', 2], ['Как зовут первого космонавта?', 'Павел Морозов', 'Эдуард Успенский', 'Алексей Леонов', 'Юрий Гагарин', 4]], 0)