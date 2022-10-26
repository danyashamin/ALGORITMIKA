first = int(input('Введите длительность первого фильма:'))#длительность первого фильма
second = int(input('Введите длительность второго фильма:'))#длительность второго фильма
cur_time = int(input('Введите текущее время:'))#текущее время

if cur_time%first < cur_time%second:
    print(cur_time%first)
    print('Иди на первый')
elif cur_time%first > cur_time%second:
    print(cur_time%second)
    print('Иди на второй')
else:
    print('Иди куда хочешь')