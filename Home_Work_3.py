# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('\nTask1')
import random

lst1 = []
for i in range(random.randint(5,10)):
    x = random.randint(1,10)
    lst1.append(x)

print(lst1)

sum = 0
for i in range(1, len(lst1), 2):
    sum += lst1[i]

print(f'Sum (with odd index) = {sum}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:- [2, 3, 4, 5, 6] => [12, 15, 16];
#        - [2, 3, 5, 6]    => [12, 15]

print('\nTask2')

# lst1 = [2, 3, 4, 5, 6]  # for control
# lst1 = [2, 3, 5, 6]     # for control
print('Список из задачи 1. Произведения: ', end='')

ln = len(lst1)
for i in range(ln):
    if i >= ln/2:
        break
    print(lst1[i] * lst1[-i-1], end=' ')

# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('\n\nTask3')

lst3 = [1.1, 1.2, 3.1, 5, 10.01, 0.002]
min_fract = lst3[0]%1
max_fract = lst3[0]%1

for i in range(1, len(lst3)):
    tmp = lst3[i]%1
    if tmp == 0:
        continue
    if min_fract > tmp:
        min_fract = tmp
    if max_fract < tmp:
        max_fract = tmp

print(f'{lst3} => ', end='')
print(round(max_fract - min_fract, 4))


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:- 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('\nTask4')

num10 = int(input('Введите число для перевода в двоичное: '))
print(bin(num10)) # check

def decimal_to_binary(n10):
    str2=''
    while n10 > 0:
        str2 += str(int(n10 % 2))
        n10 = int(n10/2)
    str3=''  # для разворота строки
    for i in range(1, len(str2)+1):
        str3 += str2[-i]
        
    return str3

print(decimal_to_binary(num10))


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


print('\nTask5')

def neg_fibonach (num, j):
    return num * (-1) ** (j+1)
 
fib1 = 0
fib2 = 1
lst5 = []
lst_neg = []
lst5.append(fib1)
lst5.append(fib2)
lst_neg.append(neg_fibonach(fib1,0))
lst_neg.append(neg_fibonach(fib2,1))

k = int(input('Введите номер элемента ряда Фибоначчи: '))

for i in range(k-1):
    fib1, fib2 = fib2, fib1 + fib2
    lst5.append(fib2)
    lst_neg.append(neg_fibonach(fib2,i))

print(lst5)     # check
print(lst_neg)  # check

lst_sum = []
for i in range(k):
    lst_sum.append(lst_neg[-i-1])
    # разворот негафибоначчи и внесение в суммарный список

for i in range(k+1):
    lst_sum.append(lst5[i])
    # добавление нормального ряда фибоначчи

print(lst_sum)
