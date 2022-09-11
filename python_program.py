from random import choice

class SpeakerWhatToDo():
    def __init__(self, name, affairs):
        self.name = name
        self.affairs = affairs
    def sayToDo(self):
        print(choice(self.affairs))
    def __call__(self):
        print('Привет, меня зовут', self.name+'.')
        print('Тебе надо:')
        self.sayToDo()
        print('Вот что делать.')

def say(name, affairs):
    speaker = SpeakerWhatToDo(name, affairs)
    def performance():
        speaker()
    return performance

decoratorObj = say('Игорь', ['Пойти погулять!'])
decoratorObjSecond = say('Сергей', ['Пойти погулять!', 'Не пойти погулять!'])
decoratorObj()
decoratorObjSecond()