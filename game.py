import random

seed = ["Камень","Ножницы","Бумага"]
computer_score = 0
player_score = 0

while computer_score < 7 and player_score < 7:
    random_seed =  random.choice(seed)
    player_choice = input("")
    if player_choice == random_seed:
        print(f"компьютер - ученик \n{random_seed} - {player_choice} \n{computer_score} - {player_score} (Ничья)")
    elif(player_choice == "Камень" and random_seed == "Ножницы") or \
        (player_choice == "Ножницы" and random_seed == "Бумага") or \
        (player_choice == "Бумага" and random_seed == "Камень"):
        player_score += 1
        print(f"компьютер - ученик \n {random_seed} - {player_choice} \n {computer_score} - {player_score}")
    else:
        computer_score += 1
        print(f"компьютер - ученик \n {random_seed} - {player_choice} \n {computer_score} - {player_score}")
if computer_score == 7 or player_score == 7:
    print("Конец игры")