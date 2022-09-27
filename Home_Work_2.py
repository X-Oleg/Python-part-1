# 1. Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('\nTask1')
dic1 = {}
n = int(input('Введите n: '))
for i in range(1, n+1):
    dic1[i] = 3*i + 1
print(dic1)

# 2. Напишите программу, которая принимает на вход число N и выдает набор 
# произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('\nTask2')
n2 = int(input('Введите N: '))
tmp = 1
print(f'N = {n2}, тогда [', end=' ')
for i in range(1, n2+1):
    tmp *= i
    print(tmp, end=', ')
print('\b\b ]')

# 3. Задайте список из n чисел последовательности (1+ (1/n))^n и выведите 
# на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

print('\nTask3')
n3 = int(input('Введите n: '))
lst3 = []
sum = 0.0
for i in range(1, n3+1):
    step = (1 + 1 / i) ** i
    lst3.append(step)
    sum += step
print(round(sum, 2), end=' ')
print(lst3)


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

print('\nTask4')
import random

n4 = int(input('Введите N: '))
lst4 = []
for i in range(1, n4+1):
    lst4.append(random.randint(-n4,n4))
print(lst4)

f = open('file.txt')
ind1 = int(f.read(1))
ind2 = int(f.read(2))
f.close()
print(f'Indexes from file.txt: {ind1}, {ind2}')

mult4 = lst4[ind1] * lst4[ind2]
print(mult4)

# 5. Реализуйте алгоритм перемешивания списка.
# (Без использования библиотеки random)

print('\nTask5')
lst5 = [1, 2, 3, 4, 5, 6, 7]

import datetime 
import time

# print(int(datetime.datetime.now().microsecond%10))
a1 = int(datetime.datetime.now().microsecond%10)

# print(int((time.time() * 256)%10))
a10 = int((time.time() * 256)%10)

import math
# Линейный конгруэнтный метод

m=32768
a=23
b=12345
# a=a1+a10*10 # случайный выбор множителя (это мои пробы)
# можно еще попробовать случайно выбирать из массива рекомендованных констант

def lin_rand_arr_flxd(seed,size):
    if size==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
    r=[0 for i in range(size)]
    r[0]=math.ceil(seed)
    for i in range(1,size):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    return r[1:size]

arr5 = (lin_rand_arr_flxd(time.time(),len(lst5)+1))
print(arr5)

def selection_sort(arr_mix, arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]
        arr_mix[minimum], arr_mix[i] = arr_mix[i], arr_mix[minimum]
        # здесь первичный массив сортируем вместе со случайным...
            
    return arr_mix
print(lst5)
print(selection_sort(lst5, arr5))   
