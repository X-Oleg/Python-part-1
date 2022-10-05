# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# str1 = 'Hello ureuvoehovhe Rkjnbk not Hello (('
# srt_target = 'Hello'

# lst = str1.split(sep=' ')
# print(lst)

# count = 0
# for i in range (len(lst)):
#     if lst[i] == srt_target:
#         count +=1

# print(count)

## replace, apper, lower ... Синтаксис: str.split (sep=None, maxsplit=-1)

# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# str2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

# count = 0
# search = "йцу "

# for i in range (len(str2)):
#     if search == str2[i]:
#         count +=1
#     if count == 2:
#         print (i)
#         break
# if count != 2:
#     print(-1)


# Задайте строку из набора чисел. Напишите программу, которая покажет большее 
# и меньшее число. В качестве символа-разделителя используйте пробел.

# str1 = '1 2 3 5 8 6'
# lst1 = str1.split()
# min = int(lst1[0])
# max = int(lst1[0])
# for i in range(1, len(lst1)):
#     if int(lst1[i]) > max:   # ???
#         max = lst1[i]
#     elif int(lst1[i]) < min:
#         min = lst1[i]
# print(min, max)

# str = '66 7 34 0 9'
# lst = str.split(sep=' ')
# max = int(lst[0])
# min = int(lst[0])
# print(lst)
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# for i in range(1,len(lst)):
#     if lst[i] > max:
#         max = lst[i]
#     if lst[i] < min:
#         min = lst[i]
# print(f'Максимальное число -{max}, Минимальное число - {min}')


# Найдите корни квадратного уравнения Ax² + Bx + C = 0

# a = int(input('Input A :'))
# b = int(input('Input B :'))
# c = int(input('Input C :'))

# decr = b**2-4*a*c

# if decr > 0:
#     x1 = (-b+decr**0.5)/(2*a)
#     x2 = (-b-decr**0.5)/(2*a)
#     print(x1, x2)
# elif decr == 0:
#     x1 = -b/(2*a)
#     print(x1)
# else:
#     print('no X')


# Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.


a = int(input('Input A :'))
b = int(input('Input B :'))

nod = 2
while True:
    if b%nod == 0 and a%nod == 0:
        print(nod)
        break
    else:
        nod +=1

if a > b:
    nok = a
else:
    nok = b

while True:
    if nok%b == 0 and nok%a == 0:
        print(nok)
        break
    else:
        nok += 1

# Найти наименьшее общее кратное через наибольший общий делитель можно 
# по формуле НОК (a,b)=a⋅b:НОД(a, b)

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append (i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")