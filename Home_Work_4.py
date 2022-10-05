# 1. Вычислить число π c заданной точностью d
# Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

print('\nTask1')

import math
print ( math.pi )

def pi_accuracy(acc, ln):
    
    den = 3
    pi_acc = 4
    tmp = 1
    i = 1
    while abs(tmp) > acc/10:
        if i % 2 == 0:
            tmp = 4 / den
        else :
            tmp = -4 / den
        pi_acc += tmp
        den += 2
        i += 1
    tmp = str(pi_acc)
    print (tmp[:ln])

accuracy = str(input('Input accuracy of PI :'))
if float(accuracy) <= 0.1:
    pi_accuracy( float(accuracy), len(accuracy) )
else:
    print('Incorrect number')


# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

print('\nTask2')

def prime_factors(n):
   i = 2
   lst_prime = []
   while i * i <= n:
       while n % i == 0:
           lst_prime.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       lst_prime.append(int(n))
   return lst_prime

num2 = int(input('Input Number :'))
print(prime_factors(num2))  


# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

print('\nTask3')

import random

lst3 = []
for i in range(random.randint(7,14)):
    x = random.randint(1,9)
    lst3.append(x)

print(lst3)

new_lst3 =[]
for i in lst3:
    if i not in new_lst3:
        new_lst3.append(i)

print(new_lst3)
