def guess_code(password:str):

    password_list = list(password)
    attemps = 0
    max_attemps = 10
    for i in range (max_attemps):
        code = input('')
        code_list = list(code)
        if len(code_list) != 5:
            print('Ошибка! Нужно ввести ровно 5 цифр')
            continue
        attemps += 1

        if code_list == password_list:
            print('Угадано цифр: 5 \nНа своих местах: 5')
            print(f'Поздравляем! Вы угадали пароль {password} за {attemps} попыток! ')

            break
        number = 0
        for k in range (len(password_list)):
            if code_list[k] in password_list:
                number += 1
            else: number += 0

        place_number = 0
        for j in range (len(code_list)):
            if password_list[j] == code_list[j]:
                place_number += 1
            else:
                place_number += 0
        print(f'Угадано цифр: {number} \nНа своих местах: {place_number}')
        if i < 10:
            print('Неверно, попробуйте ещё раз')

    else:
        print(f'Игра окончена! \nПравильный пароль \nбыл: {password}')
guess_code("39412")