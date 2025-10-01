number = int(input())
fib_list = []
a = 0
b = 1
for i in range(number):
    fib_list.append(a)
    a, b = b, a + b
    print(fib_list)