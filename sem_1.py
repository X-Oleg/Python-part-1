## По двум заданным числам проверить является ли одно квадратом второго

## a = int(input('Input first number'))

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))

# print(b ** 2 == a or a ** 2 == b)


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))

# if b ** 2 == a:
#     print('Первое число является квадратом второго')
# elif a ** 2 == b:
#     print('Второе число является квадратом первого')
# else:
#     print('Одно число не является квадратом второго')

# ## Найти максимальное из пяти чисел

# lst = [1,6,8,10,65]
# max = lst[0]
# for i in range(0,5): # range(len(lst)
#     if lst[i] > max:
#         max = lst[i]
# print(max)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input('Введите n: '))
# for i in range(-n,n+1):
#     print(i, end=' ')


# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#


# number = float(input('Input Number :'))

# number = number * 10 % 10
# print(int(number))

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number = int(input('Введите число: '))
# print((number%5 == 0 and number%10 == 0) or (number%15 == 0 and number%30 != 0))


# Напишите программу, которая выводит нечетные числа из заданного списка
#  и останавливается, если встречает число 554.

import random

lst = [554]
for i in range(random.randint(5,10)):
    x = random.randint(500,600)
    lst.append(x)

print(lst)
random.shuffle(lst)
print(lst)

for i in lst:
    if(i == 554):
        break
    elif(i%2 != 0):
        print(i, end=' ')  ## ------------- !!!!!!!!!!!
print()


# Сложить цифры вещественного числа

number = '1.2345'
sum = 0
for i in number:
    if ( i != '.'):
        sum += int(i)
print(sum)

# Посчитайте, сколько раз символ встречается в строке

str = 'Посчитайте, сколько раз символ встречается в строке'
sum = 0
for i in str:
    if ( i == 'с'):
        sum += 1
print(sum)
