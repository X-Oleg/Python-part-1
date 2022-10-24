# # lecture 3

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc2, 7) ## 70


# sum = lambda x: x+10
# mult = lambda x: x**2

# print(sum(mult(2))) ## 14

# f = sum
# g = mult


# def h(f, g, x): return f(g(x))
# print(h(sum, mult, 7))          ## 59


# print(h(sum, mult, 5)) ## 35 

# print( h(lambda x: x+10, lambda x: x**2, 7) ) ## 59


# ## 1
# # f = open('f.txt', 'r')
# # data = f.read() + ' '
# # f.close()
# # numbers = []
# # while data != '':
# #     space_pos = data.index(' ')
# #     numbers.append(int(data[:space_pos]))
# #     data = data[space_pos+1:]
# # out = []
# # for e in numbers:
# #     if not e % 2:
# #         out.append((e,e **2))
# # print(out)

# ## 2
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)

# ## 3
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)

# ##
# ## 1
# lst = []

# for i in range(1,21):
#     if(i%2 == 0):
#         lst.append(i)

# print(lst)

# ## 2
# lst = [i for i in range(1,21) if i % 2 == 0]
# print(lst)

# lst = [(i, mult(i)) for i in range(1,21) if i % 2 == 0]
# print(lst)


# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

with open('file.txt', 'r') as rd:
    lst = list(map(int, rd.read().split(' ')))

for i in range(1, len(lst)):
    if lst[i] != lst [i-1] +1:
        lst.insert(i, lst[i]-1)

print (lst)
with open('file.txt', 'w') as rd:
    rd.write(' '.join(map(str, lst)))





# st1 = '0 1 2 3 4 6 7 8'
# lst = st1.split(' ')

# # Напишите программу, удаляющую из текста все слова, содержащие "абв".

# str = '''Напишите абв напиабв програбвмму программу, удаляющую из этого абв 
# текста все вабвс слова, содерабващие содержащие "абв"'''
# lst = list(filter(lambda x: 'абв' not in x, str.split(' ')))
# print(' '.join(lst))

