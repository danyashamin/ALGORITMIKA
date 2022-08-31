class ObjectMy():
    def __init__(self, a):
        self.a = a
    def __le__(self, other):
        return (self.a, other.a)
a = ObjectMy('a')
b = ObjectMy('b')
c = a<=b
print(c)