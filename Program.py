class A():
    def __init__(self, a):
        self.a = a

letter_1 = A('a')
letter_1.b = 'Я с ней не дружу!'
print(letter_1.b)