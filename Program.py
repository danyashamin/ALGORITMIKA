class Animal():
    def __init__(self, typeAnimal, strenght):
        self.typeAnimal = typeAnimal
        self.strenght = strenght
    def __add__(self, otherAnimal):
        print('Привет, ', otherAnimal.typeAnimal, ', я - '+self.typeAnimal)
        print('Давай дружить')
    def __lt__(self, otherAnimal):
        if self.strenght<otherAnimal.strenght:
            print('Я тебя боюсь!')
        else:
            print('Не боюсь я тебя!')
    
hare = Animal('Заяц', 2)
wolf = Animal('Волк', 4)
a = hare<wolf
b = hare+wolf