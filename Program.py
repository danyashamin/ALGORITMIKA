def service(func_service):
    def service_performance():
        func_service()
        print('С вас тыщ!')
    return service_performance

@service
def hair_cut():
    print('Я постриг тебе волосы.')
def shaving():
    print('Я побрил тебя.')

service_type = input(f'Какую услугу вы желаете?\n')
qlossery = {'стрижку':hair_cut, 'бритьё':shaving}
service_obj = service(qlossery[service_type])
question = input(f'Выполнить?\n')
if question == 'да':
    service_obj()