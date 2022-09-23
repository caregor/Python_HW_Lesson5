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
# def draw_lots():
#     return random.randint(0, 1)
#
#
# def check_input(count, candies):
#     if 0 < candies < 29 and count >= candies:
#         return True
#     else:
#         return False
#
#
# def play_with_bot():
#     bot_value = input('Do you want to play with bot? (yes/no)')
#     if bot_value == 'yes':
#         return True
#     else:
#         return False
#
#
# def step(candy, player1, player2):
#     correct_flag = False
#     if player1['draw']:
#         # print("Player one's step")
#         candy_points_player_one = int(input(f"{player1['name']}, Please! take a candy:"))
#         correct_flag = check_input(candy, candy_points_player_one)
#         candy_points_player_two = 0
#         if correct_flag:
#             player1['draw'] = 0
#             player2['draw'] = 1
#             player1['points'] = int(player1['points']) + candy_points_player_one
#     else:
#         # print("Playes two's step")
#         if player2['bot'] == False:
#             candy_points_player_two = int(input(f"{player2['name']}, Please! take a candy:"))
#         else:
#             if candy > 29:
#                 candy_points_player_two = random.randint(1, 28)
#             else:
#                 candy_points_player_two = random.randint(1, candy)
#             print(f'Bot takes {candy_points_player_two}')
#         correct_flag = check_input(candy, candy_points_player_two)
#         candy_points_player_one = 0
#         if correct_flag:
#             player1['draw'] = 1
#             player2['draw'] = 0
#             player2['points'] = int(player2['points'] + candy_points_player_two)
#     if correct_flag:
#         return candy - candy_points_player_one - candy_points_player_two
#     else:
#         print('Incorrect takes candy. Read the rules for games. Or you take more candies than exist.')
#         return candy
#
#
# with open('source02', 'r') as file:
#     for line in file:
#         print(line.strip())
# print()
#
# player_one = dict(name='player one', draw=0, points=0, bot=False)
# player_two = dict(name='player two', draw=0, points=0, bot=False)
# candies = 56
# draw_mark = False
#
# player_two['bot'] = play_with_bot()
#
# while candies > 0:
#
#     if not draw_mark:
#         print('Choose Who will be first..')
#         flip = draw_lots()
#         draw_mark = True
#         if flip != 0:
#             player_one['draw'] = 1
#             print('The first step will make ', player_one['name'].upper())
#             print()
#         else:
#             print('The first step will make ', player_two['name'].upper())
#             print()
#     candies = step(candies, player_one, player_two)
#     print(candies, 'left')
# if player_one['draw'] != 1:
#     print(f"Player one WINNER!!! and he takes {player_one['points']} candies.")
# else:
#     print(f"Player two WINNER!!! and he takes {player_two['points']} candies")

# Задача №3
# def present_table():
#     print(' 1 | 2 | 3\n'
#           '----------\n'
#           ' 4 | 5 | 6\n'
#           '----------\n'
#           ' 7 | 8 | 9 ')
#
#
# def play_table(play_list):
#     print('Play Table')
#     print(
#         f'{play_list[0]} | {play_list[1]} | {play_list[2]}\n'
#         '---------\n'
#         f'{play_list[3]} | {play_list[4]} | {play_list[5]}\n'
#         '---------\n'
#         f'{play_list[6]} | {play_list[7]} | {play_list[8]}\n')
#
#
# def flip():
#     coin = random.randint(0, 1)
#     print('How will be first....')
#     if coin:
#         print('player 1 will first...')
#         return True
#     else:
#         print('player 2 will first...')
#         return False
#
#
# def check_step(step, data):
#     if data[int(step) - 1] != ' ':
#         print('Wrong Step. Please try again')
#         return False
#     else:
#         return True
#
#
# def make_step(flip_flop, data):
#     while True:
#         if flip_flop:
#             value = input('player 1 step (X):')
#             if 0 < int(value) < 10:
#                 if check_step(value, data):
#                     data.pop(int(value) - 1)
#                     data.insert(int(value) - 1, 'X')
#                     break
#             else:
#                 print('Wrong Enter. Please Enter 1..9')
#         else:
#             value = input('player 2 step (O):')
#             if 0 < int(value) < 10:
#                 if check_step(value, data):
#                     data.pop(int(value) - 1)
#                     data.insert(int(value) - 1, 'O')
#                     break
#             else:
#                 print('Wrong Enter. Please Enter 1..9')
#     return data
#
#
# print()
# current_step = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#
#
# def check_winner(steps, data):
#     if steps < 5:
#         if data[0] == data[1] == data[2] or data[3] == data[4] == data[5] or data[6] == data[7] == data[8] or data[0] == \
#                 data[3] == data[6] or data[1] == data[4] == data[7] or data[2] == data[5] == data[8] or data[0] == data[
#             4] == data[8] or data[6] == data[4] == data[2]:
#             print('You WIN!!! Finish him...')
#             return True
#         else:
#             return False
#     return None
#
#
# order = flip()
# present_table()
# print()
# mark = 0
# step = 8
# play_table(current_step)
# if order and mark == 0:
#     print('Player 1 make a step (choose 1..9):')
#     current_step = make_step(order, current_step)
#     mark = 1
#     order = 0
# else:
#     print('Player 2 make a step (choose 1..9):')
#     current_step = make_step(order, current_step)
#     mark = 1
#     order = 1
#
# present_table()
# play_table(current_step)
# while step > 0:
#
#     current_step = make_step(order, current_step)
#     if order:
#         order = 0
#     else:
#         order = 1
#
#     present_table()
#     print()
#     play_table(current_step)
#     step = step - 1
#     winner = check_winner(step, current_step)
#     if winner:
#         break

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
