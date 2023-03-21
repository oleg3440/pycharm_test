# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

a = int(input('Введите количество конфет'))
hod = 0
wins = {0: 'Игрок', 1: 'Бот'}
while a > 0:
    if a <= 28:
        print(f'Выиграл {wins[hod]}')
        break
    if hod % 2 == 0:
        print('Ход Игрока')
        d = int(input('Введите количество конфет, которое хотите взять'))
        a -= d
        print(f'Осталось конфет: {a}')
    else:
        print('Ход Бота')
        d = a % 29
        a -= d
        print(f'Осталось конфет: {a}')
    hod = (hod + 1) % 2






Вариант 2
import random


def MoveHuman(move):
    count = 0
    while (count <= 0 or count > 28):
        count = int(input(f'Ход {move} игрока: '))
        if (count <= 0 or count > 28):
            print("Неправильное число конфет")
    return count


def MoveEasy(move):
    count = random.randint(1, 28)
    print(f'Ход {move} игрока: {count}')
    return count


def MoveHard(candy, move):
    if candy % 29 == 0:
        count = random.randint(1, 28)
    else:
        count = candy % 29
        if count == 0:
            count = 1
    print(f'Ход {move} игрока: {count}')
    return count


def Game(candy, difficulty):
    move = random.randint(0, 1)
    while (candy > 0):
        print(f'Конфет - {candy}')
        move = move % 2 + 1
        if move == 1:
            candy -= MoveHuman(move)
        else:
            if difficulty == 1:
                candy -= MoveHuman(move)
            elif difficulty == 2:
                candy -= MoveEasy(move)
            elif difficulty == 3:
                can
