class ObjectMy():
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        print('Выполнилось')
        return (self.a, other.a)
a = ObjectMy('a')
b = ObjectMy('b')
c = a==b
print(c)