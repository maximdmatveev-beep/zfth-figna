while True:
    number_tiles = input("Enter a tiles number: ")
    if number_tiles.isdigit():
        number_tiles = int(number_tiles)
        if number_tiles % 2 == 0:
            if number_tiles == 0:
                print(" ")
            else:
                for i in range(number_tiles):
                    for j in  range(number_tiles):
                        if (i+j) % 2 == 0:
                            print('■', end=' ')
                        else:
                            print('□', end=' ')
                    print()
        else:
            print('неверный ввод, введите четное число')
            continue

    else:
        print('неверно, введите целое число')
        continue
    break


