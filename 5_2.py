# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько 
# конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота 'интеллектом'

import random

print('''    Привет! Это игра с конфетами! 
    Правила: На столе лежит 150 конфет. Играют два игрока, делая ход друг после друга.
    Первый ход определяется жеребьёвкой.
    За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход!
    Ну что ж, поехали! :=)))''')

total_candy = 150
max_to_take = 28

player_1 = input("Как зовут первого игрока?: ")
player_2 = input("Как зовут второго игрока?: ")

def take_candies(player, max):
    step = int(input(f"{player}, возьми не больше {max} конфет => "))
    while step < 1 or step > max:
        step = int(input(f"{player}, столько конфет брать нельзя, попробуй еще раз! => "))
    return step

def player_turn(player, step, total):
    print(f"Ходил игрок {player}, он взял {step} конфет. На столе осталось {total} конфет.")

def player_to_player(pl_1,pl_2, total, max):
    print("Жеребьевка! Кто же первый начнет игру?")
    lottery = random.randint(0,1)
    if lottery == 0:
        first = pl_1
        second = pl_2
    else:
        first = pl_2
        second = pl_1
    print(f"Итак, первый ход за {first}!")

    priority = 0

    while total > 0:
        if priority == 0:
            step = take_candies(first, max)
            total -= step
            priority = 1
            player_turn(pl_1, step, total)
        else:
            step = take_candies(second, max)
            total -= step
            priority = 0
            player_turn(pl_2, step, total) 

    if priority == 0:
        print(f"Выиграл {first}!")
    else:
        print(f"Выиграл {second}!")

player_to_player(player_1, player_2, total_candy, max_to_take)