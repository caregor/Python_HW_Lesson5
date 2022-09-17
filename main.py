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


# Задача №1
# with open ('source01', 'r') as file:
#     source_str = file.read().split()
#
# with open('result01', 'w') as file:
#     file.write(' '.join([word for word in source_str if 'абв' not in word]))

# Задача №4
def rle_code(data):
    encoding_data = ''
    prev_symbol = ''
    count = 1

    for symbol in data:
        if symbol != prev_symbol:
            if prev_symbol:
                encoding_data += str(count) + prev_symbol
            count = 1
            prev_symbol = symbol
        else:
            count += 1
    else:
        encoding_data += str(count) + prev_symbol
        return encoding_data


def rle_decode(data):
    decode = ''
    count = ''
    for symbol in data:
        if symbol.isdigit():
            count += symbol
        else:
            decode += symbol * int(count)
            count = ''
    return decode


with open('source04', 'r') as file:
    data_source = file.read()

with open('result04', 'w') as file:
    file.write(rle_code(data_source))

with open('result04', 'r') as file:
    data_for_decode = file.read()

with open('result04_1', 'w') as file:
    file.write(rle_decode(data_for_decode))
