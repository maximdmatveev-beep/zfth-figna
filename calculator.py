number1 = input('введите первое число ')
operator = input('введите знак ')
number2 = input('введите второе число ')
while True:
    try:
        number1 = float(number1)
        number2 = float(number2)

        if operator == '*':
            result = number1 * number2
        elif operator == '/':
            if number2 == 0:
                print("Ошибка!")
            else:
                result = number1 / number2
        elif operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        else:
            print("Ошибка!")
        print(result)
    except ValueError:
        print("Ошибка!")
    break