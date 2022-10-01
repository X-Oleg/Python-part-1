# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str1 = 'Hello ureuvoehovhe Rkjnbk not Hello (('
srt_target = 'Hello'

lst = str1.split(sep=' ')
print(lst)

count = 0
for i in range (len(lst)):
    if lst[i] == srt_target:
        count +=1

print(count)

## replace, apper, lower ... Синтаксис: str.split (sep=None, maxsplit=-1)

# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


str2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

count = 0
search = "йцу "

for i in range (len(str2)):
    if search == str2[i]:
        count +=1
    if count == 2:
        print (i)
        break
if count != 2:
    print(-1)

