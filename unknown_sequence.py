n1 = int(input())
n2 = int(input())
N = int(input())
a = 0
seq_list = [n1, n2]
for i in range(N-2):
    a = n1 + n2 + n1 * n2
    seq_list.append(a)
    n1 = n2
    n2 = a
print(seq_list)
