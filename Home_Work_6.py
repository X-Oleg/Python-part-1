# 1. Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('\nTask1(2)')

dic1 = {}
n = int(input('Введите n: '))
for i in range(1, n+1):
    dic1[i] = 3*i + 1
print(dic1)

## new version
dic2 = {i: 3*i+1 for i in range(1, n+1)}
print(dic2)


# 3. Задайте список из n чисел последовательности (1+ (1/n))^n и выведите 
# на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

print('\nTask3(2)')
n3 = int(input('Введите n: '))

lst3 = []
sum = 0.0
for i in range(1, n3+1):
    step = (1 + 1 / i) ** i
    lst3.append(step)
    sum += step
print(round(sum, 2), end=' ')
print(lst3)

## new version
import math

lst3_1 = [(1 + 1 / i) ** i for i in range(1, n3+1)]
print(round(math.fsum(lst3_1), 2), lst3_1)


# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('\n\nTask3(3)')

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

## new version

new_lst3 = [round(i%1, 3) for i in lst3 if i%1 != 0]
print(f'{lst3} => {max(new_lst3) - min(new_lst3)}')

