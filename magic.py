class Object_my():
    def __init__(self, file_name):
        self.file = open(file_name)
    def __ne__(self, other):
        if self.file != other.file:
            print('Да, неравен!')
        else:
            print('Нет, равен!')
    def __del__(self):
        print('Щас закроем')
        if self.file.closed == False:
            print('Есть.')
            self.file.close()

obj_1 = Object_my('text.txt')
obj_2 = Object_my('text.txt')