# 4(4). Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²


print('\nTask4(4)')
import random

def write_file(f_name, dt):
    with open(f_name, 'w') as data:
        data.write(dt)

def rand():
    return random.randint(0,100)

def create_mult(k):
    lst = [rand() for i in range(k+1)]
    return lst
    
def create_polynom(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input('Input k = '))
mults = create_mult(k)
write_file('file4(4).txt', create_polynom(mults))
print(create_polynom(mults))


# # 5(4) Даны два файла, в каждом из которых находится запись многочлена. 
# # Задача - сформировать файл, содержащий сумму многочленов.

print('\nTask5(4)')

# will use previous functions and 1. polynomial

# degree of polynom
def degree_polynom(k):
    if  'x^'in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k ) and ('^' not in k):
        num = 1
    else:
        num = - 1
    return num

# extract koef member of polynomial
def k_polynom(k):
    if  'x'in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# analysis polynomial extract all koef
def calc_polynom(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    ln = len(st)

    if degree_polynom(st[-1]) == -1:
        lst.append(int(st[-1]))
        ln -= 1

    i = 1               # degree
    ind = ln-1          # inrex
    while ind >= 0:
        if degree_polynom(st[ind]) != - 1 and degree_polynom(st[ind]) == i:
            lst.append(k_polynom(st[ind]))
            ind -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    


# create 2 file
k2 = int(input('Input k2 = '))
mults2 = create_mult(k2)
write_file('file5(4).txt', create_polynom(mults2))

# calculate sum of polynoms
with open('file4(4).txt', 'r') as data:
    st1 = data.readlines()
with open('file5(4).txt', 'r') as data:
    st2 = data.readlines()
print(f'1 polynomial: {st1}')
print(f'2 polynomial: {st2}')
lst1 = calc_polynom(st1)
lst2 = calc_polynom(st2)

i_start = len(lst1)
if i_start > len(lst2):
    i_start = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(i_start)]
if len(lst1) > len(lst2):
    i_end = len(lst1)
    for i in range(i_start,i_end):
        lst_new.append(lst1[i])
else:
    i_end = len(lst2)
    for i in range(i_start,i_end):
        lst_new.append(lst2[i])
write_file('file5(result).txt', create_polynom(lst_new))
with open('file5(result).txt', 'r') as data:
    st3 = data.readlines()
print(f'Result polynomial: {st3}')


# 1(5). Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# б) Подумайте, как наделить бота "интеллектом"

# вариант человек против человека:

print('\nTask1(5)')
from random import randint

def input_quantity(name):
    x = int(input(f'{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет (от 1 до 28): '))
    return x


def step_print(name, k, counter, value):
    print(f'Ходил {name}, он взял {k}, теперь у него {counter}. Осталось {value} конфет.')

def play(function, second = 'human'):
    player1 = input('Введите имя первого игрока: ')
    if second == 'human':
        player2 = input('Введите имя второго игрока: ')
    else:
        player2 = 'Bot'
    value = int(input('Введите количество конфет на столе: '))
    flag = randint(0,2) # очередность
    if flag:
        print(f'Первый ходит {player1}')
    else:
        print(f'Первый ходит {player2}')

    counter1 = 0  
    counter2 = 0

    while value > 28:
        if flag:
            k = input_quantity(player1)
            counter1 += k 
            value -= k
            flag = False
            step_print(player1, k, counter1, value)
        else:
            if second == 'human':
                k = function(player1)
            elif second == 'Bot':
                k = function(1, 29)
            else:
                k = function(value)
            counter2 += k
            value -= k
            flag = True
            step_print(player2, k, counter2, value)

    if flag:
        print(f'Выиграл {player1}')
    else:
        print(f'Выиграл {player2}')

play(input_quantity)

# # a) Добавьте игру против бота

print('\nTask1(5)a')
play(randint, 'Bot')

# # б) Подумайте, как наделить бота "интеллектом"

print('\nTask1(5)b')

def bot_calc(value):
    k = value % 28 - 1
    if k+1 == 0 or k == 0:
        k = 1
    return k

play(bot_calc, 'Bot_calc')


# 3(5). Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 

print('\nTask3(5)')

def rle_code(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: return '' 
    for char in data: 
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + prev_char 
    return encoding


def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode
       
s = input('Введите текст для кодировки: ')

print(f'Текст после кодировки: {rle_code(s)}')
print(f'Текст после дешифровки:      {rle_decode(rle_code(s))}')


# 2(5). Создайте программу для игры в ""Крестики-нолики""

print('\nTask2(5)')

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Выбеите номер, куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта позиция уже занята. Введите свободный номер.")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (f'\nПоздравляю!  - - - - - - - - - {tmp}, выиграл!\n')
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)

