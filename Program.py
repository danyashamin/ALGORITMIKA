from multiprocessing import managers


class Manager():
    def __init__(self, Name, suggestions):
        self.Name = Name
        self.suggestions = suggestions
    def __call__(self):
        print('My suggestions:', self.suggestions)

managerFirst = Manager('Игорь', ['пойти погулять', 'не пойти погулять'])
managerFirst()