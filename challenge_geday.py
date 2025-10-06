import random

letter = ["С","Т"]
seq = []
for i in range(5):
    random_letter = random.choice(letter)
    seq.append(random_letter)
print(seq)

def check(seq: list) -> str:
    student = input("свет или тьма: ").lower()
    result = seq.count("С")
    if (result >= 3 and student == "свет") or (result < 3 and student == "тьма"):
        print('Падаван достоин звания "Рыцаря-джедая"!')
    else:
        print('Падаван остаётся на дополнительное обучение...')
check(seq)
