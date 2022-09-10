def decorator(func_1, func_2):
    def performance():
        func_1()
        print('Ещё выполни!')
        func_2()
    return performance
def say_hello():
    print("Hello. ", end='')
def say_goodbye():
    print('Goodbye')
def say_something():
    print('привет')

func_obj = decorator(say_hello, say_goodbye)
func_obj()
func_obj_2 = decorator(say_hello, say_something)
func_obj_2()