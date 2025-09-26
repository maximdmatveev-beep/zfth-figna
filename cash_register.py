quantity = input("введите число товаров ")
while True:
    if quantity.isdigit():
        quantity = int(quantity)
        total = 0
        for i in range(quantity):
            price = input(f'{i+1}')
            while True:
                if price.isdigit():
                    price = int(price)
                    total += price
                    break
                else:
                    print("Ошибка")

        print(f"{total}.руб.")

        if total >= 500:
            discount = 0
            discount_text = 'нет'
            total_amount = total
        elif total % 13 == 0 or total % 101 == 0:
            discount = 31
            discount_text = '31%'
            total_amount = total * 0.69
        else:
            discount = 5
            discount_text = '5%'
            total_amount = total * 0.95
        print(f"Скидка: {discount_text}")
        print("Итоговая сумма")
        print(f'{total_amount:.2f}')
        print(f"Количество товаров:{quantity}")
        average_price = total / quantity
        print(f"Средняя цена за товар:: {average_price:.2f}")
        break
    else:
        print("Ошибка")