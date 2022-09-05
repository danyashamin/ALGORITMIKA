class Manage:
    def __call__(self, suggesting):
        print('I suggest something...')
        suggesting()
def suggesting_1():
    print('Go for a walk!')
manage_1 = Manage()
manage_1(suggesting_1)