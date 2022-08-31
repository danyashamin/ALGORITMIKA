class SprotMen():
    def __init__(self, awards):
        self.awards = awards
    def __gt__(self, otherSportMen):
        return len(self.awards)>len(otherSportMen.awards)

sprotmenOne = SprotMen(['Кубок', 'Медаль'])
sportmenTwo = SprotMen(['Грамота за "Русский медвежонок"'])
condition = sprotmenOne>sportmenTwo
print(condition)