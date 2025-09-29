number = int(input(""))
number = str(number)
reversed_the_intered_number = number[::-1]
if number == reversed_the_intered_number:
    print("Число палиндром")
else:
    print("Число не палиндром")