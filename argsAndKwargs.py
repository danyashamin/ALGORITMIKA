def func(**dict_arguments):
    for key, value in zip(dict_arguments.keys(), dict_arguments.values()):
        print('Увлечение-', key)
        print('Стоимость-', value)

dict_hobbies = dict()

cur_hobby = input('Увлечение:')
while cur_hobby!='хватит':
    cur_price = input('Цена:')
    dict_hobbies[cur_hobby] = cur_price
    cur_hobby = input('Увлечение:')
func(a='a', b='b')