def record(func):
    def cycleRecotd():
        func()
    return cycleRecotd
@record
def funcArgOne():
    print(1)
def funcArgTwo():
    print(2)
funObj = record(funcArgOne)
funObj()
funcObjSecond = record(funcArgTwo)
funcObjSecond()