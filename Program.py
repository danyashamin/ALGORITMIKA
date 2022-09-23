class Player(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return self.age - other.age
p1 = Player('Игорь', 12)
p2 = Player('Анна', 13)
print(p1 > p2)