from msilib.schema import Condition


class ProgramObj():
    def __init__(self, ObjName):
        self.file = open(ObjName)
    def __eq__(self, otherObj):
        if self.file.name == otherObj.file.name:
            print('Они равны.')
    def __del__(self):
        print(self.file.closed)
        self.file.close()
        print(self.file.closed)

obj = ProgramObj('pyqt5_program.py')
obj_2 = ProgramObj('pyqt5_program.py')
condition = obj == obj_2