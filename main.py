"""
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    a) Добавьте игру против бота
    b) Подумайте как наделить бота ""интеллектом""

3. Создайте программу для игры в ""Крестики-нолики"".

4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.
"""
import random


# Задача №1
# with open ('source01', 'r') as file:
#     source_str = file.read().split()
#
# with open('result01', 'w') as file:
#     file.write(' '.join([word for word in source_str if 'abc' not in word]))

# Задача №2
def draw_lots():
    return random.randint(0, 1)


def check_input(count, candies):
    if 0 < candies < 29 and count >= candies:
        return True
    else:
        return False


def step(candy, player1, player2):
    correct_flag = False
    if player1['draw']:
        # print("Player one's step")
        candy_points_player_one = int(input(f"{player1['name']}, Please! take a candy:"))
        correct_flag = check_input(candy, candy_points_player_one)
        candy_points_player_two = 0
        if correct_flag:
            player1['draw'] = 0
            player2['draw'] = 1
            player1['points'] = int(player1['points']) + candy_points_player_one
    else:
        # print("Playes two's step")
        candy_points_player_two = int(input(f"{player2['name']}, Please! take a candy:"))
        correct_flag = check_input(candy, candy_points_player_two)
        candy_points_player_one = 0
        if correct_flag:
            player1['draw'] = 1
            player2['draw'] = 0
            player2['points'] = int(player2['points'] + candy_points_player_two)
    if correct_flag:
        return candy - candy_points_player_one - candy_points_player_two
    else:
        print('Incorrect takes candy. Read the rules for games. Or you take more candies than exist.')
        return candy


with open('source02', 'r') as file:
    for line in file:
        print(line.strip())
print()

player_one = dict(name='player one', draw=0, points=0)
player_two = dict(name='player two', draw=0, points=0)
candies = 56
draw_mark = False
while candies > 0:
    if not draw_mark:
        print('Choose Who will be first..')
        flip = draw_lots()
        draw_mark = True
        if flip != 0:
            player_one['draw'] = 1
            print('The first step will make ', player_one['name'].upper())
            print()
        else:
            print('The first step will make ', player_two['name'].upper())
            print()
    candies = step(candies, player_one, player_two)
    print(candies, 'left')
if player_one['draw'] != 1:
    print(f"Player one WINNER!!! and he takes {player_one['points']} candies.")
else:
    print(f"Player two WINNER!!! and he takes {player_two['points']} candies")

# Задача №4
# def rle_code(data):
#     encoding_data = ''
#     prev_symbol = ''
#     count = 1
#
#     for symbol in data:
#         if symbol != prev_symbol:
#             if prev_symbol:
#                 encoding_data += str(count) + prev_symbol
#             count = 1
#             prev_symbol = symbol
#         else:
#             count += 1
#     else:
#         encoding_data += str(count) + prev_symbol
#         return encoding_data
#
#
# def rle_decode(data):
#     decode = ''
#     count = ''
#     for symbol in data:
#         if symbol.isdigit():
#             count += symbol
#         else:
#             decode += symbol * int(count)
#             count = ''
#     return decode
#
#
# with open('source04', 'r') as file:
#     data_source = file.read()
#
# with open('result04', 'w') as file:
#     file.write(rle_code(data_source))
#
# with open('result04', 'r') as file:
#     data_for_decode = file.read()
#
# with open('result04_1', 'w') as file:
#     file.write(rle_decode(data_for_decode))
