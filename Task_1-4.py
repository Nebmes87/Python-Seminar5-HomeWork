# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line_text = [str(i) for i in input('Введите текст: ').split()]
find_text = input('Введите буквы, слова с содержанием которых будут удалены: ')
new_line = []
count = 0
for item in line_text:
    if item.find(find_text) == -1:
        new_line.append(item)

print(' '.join(new_line))

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random


def lottery():
    user_input = 2
    random_number = random.randint(0, 1)
    while user_input != 0 and user_input != 1:
        user_input = int(input('Для жеребьевки выберите число 1 или 0: '))

    if random_number == user_input:
        print(f'Первым ходит тот кто выбрал {user_input}')
    else:
        print(f'Первым ходит тот кто выбрал {random_number}')


def the_game(numbers_of_candies: int):
    pool_candies = numbers_of_candies
    count = 1
    while pool_candies != 0:
        print(f'----------{count} раунд ----------')
        pool_candies -= int(input('Сколько конфет вы берете: '))
        print(f'Осталось {pool_candies} конфет')
        count += 1
    print('Вы победили!')


print('Игра в конфеты\nПравила:\n1.Первый ход определяется жеребьёвкой ')
print('2.За один ход можно забрать не более чем 28 конфет\n3.Все конфеты оппонента достаются сделавшему последний ход.')
candies = int(input('Сколько конфет на кону: '))
lottery()
the_game(candies)

# Создайте программу для игры в ""Крестики-нолики"".
import random


def print_bord(desk: list):
    print("-" * 13)
    for i in range(3):
        print("|", desk[0 + i * 3], "|", desk[1 + i * 3], "|", desk[2 + i * 3], "|")
        print("-" * 13)


def lottery():
    user_input = None
    random_number = random.randint(0, 1)
    while user_input != 0 and user_input != 1:
        user_input = int(input('Для жеребьевки выберите число 1 для игры "X" или 0 для игры "O": '))

    if random_number == user_input:
        return user_input
    else:
        return random_number


def take_input(player_token: str):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(game_board: list):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if game_board[each[0]] == game_board[each[1]] == game_board[each[2]]:
            return game_board[each[0]]
    return False


def the_game(game_board):
    position = lottery()
    counter = position
    if position == 1:
        print('Первые ходят крестики')
    else:
        print('Первые ходят нолики')
    win = False
    while not win:
        print_bord(game_board)
        if counter % 2 != 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4 - position:
            tmp = check_win(game_board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter - position == 9:
            print("Ничья!")
            break
    print_bord(game_board)


board = list(range(1, 10))
the_game(board)
input("Нажмите Enter для выхода!")

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coder(user_input: str):
    code_str = ''
    count = 1
    for i in range(1, len(user_input)):
        if user_input[i] == user_input[i - 1]:
            count += 1
        elif user_input[i] != user_input[i - 1]:
            code_str += str(count) + user_input[i - 1]
            count = 1
    if user_input[-1] != user_input[-2]:
        count = 1
        code_str += str(count) + user_input[-1]
    else:
        code_str += str(count) + user_input[-1]
    return code_str


def decoder(coder_string: str):
    coding_list = ''
    point = 0
    for i in range(len(coder_string)):
        if coder_string[i].isalpha():
            coding_list += coder_string[point:i+1] + ' '
            point = i+1

    coding_list = [str(i) for i in coding_list.split()]
    count = 0
    tmp = ''
    result = ''
    for item in coding_list:
        if len(item) > 2:
            while item[count].isdigit():
                tmp += item[count]
                count += 1
            else:
                result += int(tmp) * item[len(item) - 1]
                count = 0
                tmp = ''
        else:
            result += int(item[0]) * item[1]
            count = 0
            tmp = ''

    return result


user_string = 'WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'


print(f'Закодированный текст [{user_string}] через алгоритм RLE --->[{coder(user_string)}]<---')

if input('Хотите декодировать текст? Да/Нет: ').lower() == 'да':
    print(f'Раскодированный текст RLE --->[{decoder(coder(user_string))}] ')
elif input('Хотите раскодировать свой RLE код? Да/Нет: ').lower() == 'да':
    print(decoder(input('Введите RLE код: ')))
else:
    print('Нет так нет')