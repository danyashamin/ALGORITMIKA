from msilib.schema import Condition


class Employee():
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
    def work(self):
        print('Выполняю работу. Моя специальность:', self.experience)
    def __call__(self):
        self.work()
        print('И моё имя:', self.name)
    def __lt__(self, other):
        print(self, other)
    def __cmp__(self, other):
        return 1+other

employee = Employee('Лёша', 'Тракторист')
employee()
condition = employee<3