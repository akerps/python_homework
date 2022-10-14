# 1. Добавьте игру против бота

import random

print('''    Привет! Это игра с конфетами! 
    Правила: На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга.
    Первый ход определяется жеребьёвкой.
    За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход!
    Ну что ж, поехали! :=)))''')

total_candy = 150
max_to_take = 28

player_1 = input("Как зовут игрока?: ")
player_2 = "Bot"

def player_step(player, max):
    step = int(input(f"{player}, возьми не больше {max} конфет => "))
    while step < 1 or step > max:
        step = int(input(f"{player}, столько конфет брать нельзя, попробуй еще раз! => "))
    return step

def player_turn(player, step, total):
    print(f"Ходил игрок {player}, он взял {step} конфет. На столе осталось {total} конфет.")

def bot_step(total):
    if total > 29:
        step = total - 29
        while step > 28:
            step %= 28
    elif total < 29:
        step = total
    return step
 
def player_to_bot(pl_1,pl_2, total, max):
    print("Жеребьевка! Кто же первый начнет игру?")
    flag = random.randint(0,2)
    if flag:
        print(f"Итак, первый ход за {pl_1}!")
    else:
        print(f"Итак, первый ход за {pl_2}!")
    
    while total > 28:
        if flag:
            step = player_step(pl_1, max)
            total -= step
            flag = False
            player_turn(pl_1, step, total)
        else:
            step = bot_step(total)  
            total -= step
            flag = True
            player_turn(pl_2, step, total) 

    if flag:
        print(f"Выиграл {pl_1}!")
    else:
        print(f"Выиграл {pl_2}!")

player_to_bot(player_1, player_2, total_candy, max_to_take)