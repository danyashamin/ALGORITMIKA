class DryCleaner():
    def __init__(self, service):
        self.sevice = dry_cleaner(service)
    def performance(self):
        self.sevice()

def dry_cleaner(service):
    def work_dry_cleaner():
        service()
    return work_dry_cleaner
@dry_cleaner
def cleaning_outwear():
    print('Мы почистили вашу вернюю одежду!')
def cleaning_baby_clothes():
    print('Мы почистили одежду ваших детей!')

services = {'чистка верхней одежды':cleaning_outwear, 'чистка детских вещей':cleaning_baby_clothes}
serviceType = input('Что желаете?')
dryCleanerFirst = DryCleaner(services[serviceType.lower()])
dryCleanerFirst.performance()