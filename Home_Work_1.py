# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:- 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Input number of week`s day :'))
if (0 < day <6):
    print(f'- {day} -> No')
elif (day == 6 or day == 7):
    print(f'- {day} -> Yes')
else:
    print('Uncorrect Number')


# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).
# Пример:- x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Input X coordinate :'))
y = int(input('Input Y coordinate :'))

if ( x > 0 and y > 0 ):
    print(f'x= {x}; y= {y} -> 1')
elif ( x < 0 and y > 0 ):
    print(f'x= {x}; y= {y} -> 2')
elif ( x < 0 and y < 0 ):
    print(f'x= {x}; y= {y} -> 3')
elif ( x > 0 and y < 0 ):
    print(f'x= {x}; y= {y} -> 4')
elif ( x == 0 ):
    print(f'x= {x}; y= {y} -> Х axis')
else:
    print(f'x= {x}; y= {y} -> Y axis') # по условиям Х и У одновременно ≠ 0


# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

q = int(input('Input number of Quoter :'))

match q:
    case 1:
        print(' X > 0 and Y > 0')
    case 2:
        print(' X < 0 and Y > 0')
    case 3:
        print(' X < 0 and Y < 0')
    case 4:
        print(' X > 0 and Y < 0')
    case _:
        print('Uncorrect number')

# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:- A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def distance (a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

a = [3, 6]; b = [2, 1]

print(f'A {a}; B {b} -> {round(distance(a, b), 3)}')

a = [7, -5]; b = [1, -1]

print(f'A {a}; B {b} -> {round(distance(a, b), 3)}')


# Напишите программу для. проверки истинности 
# утверждения ¬(X V Y V Z) = ¬X ^ ¬Y ^ ¬Z для всех значений предикат.

for x in range (2):
    for y in range (2):
        for z in range (2):
            print((x, y, z), not (x or y or z) == (not x and not y and not z))
            