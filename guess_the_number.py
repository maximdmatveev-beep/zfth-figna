def bin_search(rand_num: int):
    while True:
        number = int(input(''))
        if number > rand_num:
            print(f'Неверно! Число меньше {number}')
        elif number < rand_num:
            print(f'Неверно! Число больше {number}')
        else:
            print('Верно!')
            break

bin_search(50)
