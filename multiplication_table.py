while True:

    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)

        if number == 0:
            print('0 x 0 = 0')
        else:
            for i in range(number + 1):
                for j in  range(number + 1):
                    n=i*j
                    print(f"{i}x{j}={n}")
                print()
        break
    else:
        print("Enter a valid number")
