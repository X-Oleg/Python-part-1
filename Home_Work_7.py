## user interface

# функция получает 1 или 2, как выриант выбора типа вычисления
# 1 - рациональные вычисления
# 2 - комплексные вычисления
# и возвращает целое число 1 или 2

def type_operation(): 

    print('''Выберите тип вычисления: если рациональные введите 1, 
                          если комплексные введите 2 ''') 
    while True:        
        try:
            type_calc = int(input("Ввведите число 1 или 2: "))
            if type_calc == 1 or type_calc == 2:
                return type_calc
            else:
                print('Введите либо 1 либо 2. Другие числа не подойдут. -', end=' ')
        except:
            print('Введите только целые числа (кнопки на клавиатуре): 1 или 2 -', end=' ')

# print(type_operation())   # check

# Функция возвращает только целые числа для представления
# комплексных или натуральных чисел (вещественной и мнимой части 
# или числителя и знаменателя)

def input_int():
    while True:        
        try:
            number = int(input())
            return number            
        except:
            print('Введите только целые числа (цифры):', end=' ')

# print(input_int())        # check


# Функция возвращает список из двух целых чисел
# список представляет: либо вещественную [0] и мнимую части [1]
# либо числитель [0] и знаменатель [1] натурального числа

def num_list(num):
    num = [0,0]
    print('введите первую часть числа:', end=' ')
    num[0] = input_int()
    print('введите вторую часть числа:', end=' ')
    num[1] = input_int()
    return num


def input_operation():
    while True:        
        try:    
            oper = input('Введите знак операции: "+" "-" "/" или "*"')
            if oper == "+" or oper == "-" or oper == "/" or oper == "*":
                return oper
        except:
            print('Не тот знак...')       

# print(input_operation())    # check

# Функция возвращает символ операции
# только "+" "-" "/" или "*"

  
# функция передает для дальнейшего расчета
# через глобальные переменные
#  - тип операции: 1 - рациональные вычисления, 2 - комплексные вычисления
# 
#  - символ операции: только "+" "-" "/" или "*"
# 
#  - два числа для расчета операции. Каждое в виде списка из двух целых чисел
# 

def ui_calc():

    # global 
    global type_oper
    global char_oper
    global number_1
    global number_2

    char_oper = ''
    number_1 = [0,0]
    number_2 = [0,0]

    type_oper = -1
    type_oper = type_operation()

    # input 1 number
    print('\nВведите первoe число.          ', end='      ')
    if type_oper == 1:
        print('рациональные вычисления')
        print('необходимо ввести числитель и знаменатель')
        print('если число целое. Например "7", тогда знаменатель "1"')
        print('если десятичная дробь: например "10.18" то числитель "1018" и знаменатель "100"\n')
    elif type_oper == 2:
        print('комплексные вычисления')
        print('необходимо ввести по очереди вещественную и мнимую часть')
        print('например: "7 - 3i". Сначала ввести "7" и следом "-3"\n')
    else:
        print('ошибка в функции type_operation()')
        return -1   
    number_1 = num_list(number_1)  
    
    # input operation
    print()
    char_oper = input_operation()

    # input 2 number
    print('\nАналогично первому числу ввести второе число')
    number_2 = num_list(number_2) 
    

ui_calc()                                       # check
print(f'\nCheck number1 - {number_1}')          # check
print(char_oper)                                # check
print(f'Check number2 - {number_2}')            # check
