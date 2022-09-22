# print('Hello word!')

# поиск макс и мин индексов

Numbers = [1,4,8,3,2,7]
size = len(Numbers)
print (Numbers)

i=1
maxIndex = 0
minIndex = 0

while i<size :
    if Numbers[i] > Numbers[maxIndex]:
        maxIndex = i
    elif Numbers[i] < Numbers[minIndex]:
        minIndex = i
    i=i+1

print (f'Max Index {maxIndex}, Min Index {minIndex}')


# + Найти сумму элементов массива, лежащих между максимальным и
# минимальным по значению элементами (вместе с кодом выше!)

i=0
sum = 0
if minIndex < maxIndex :
	i = minIndex +1
	stopIndex = maxIndex
else :
	i = maxIndex +1
	stopIndex = minIndex
while i < stopIndex :
	sum = sum + Numbers[i]
	i=i+1

print (f'Sum {sum}')


# Задание на «разворот» массива. Нужно перевернуть массив и
# записать его в обратном порядке.

## Numbers = [1,4,8,3,2,7]
j = len(Numbers) - 1
i=0
print (Numbers)

while i < j :
	temp = Numbers[i]
	Numbers[i] = Numbers[j]
	Numbers[j] = temp
	i = i + 1
	j = j - 1
print (Numbers)

# Найти среднее арифметическое среди всех элементов массива.

## Numbers = [1,4,8,3,2,7]
size = len(Numbers)
i=0
sum = 0
print (Numbers)

while i < size :
	sum = sum + Numbers[i]
	i = i + 1
avgArray = sum / size
	
print (avgArray)

# from lecture

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

##

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(f'{i} ') # 100 80 60 40 20

##

a = int(input('Введите а: '))
b = float(input('Введите b: '))
c = round(a + b, 2)
print('{1} + {0} = {2}'.format(b, a, c))

##

f = [1,2,34]
print(f)
print(not 3 in f) ## True
print(not 2 in f) ## False

is_odd = f[0] % 2 == 0 ## False
print(is_odd)
is_odd = not f[0] % 2 ## Phython style
print(is_odd)

##

original = int(input('Введите а: '))
inverted = 0
while original != 0:
	inverted = inverted * 10 + (original % 10)
	original //=10
print(inverted)

