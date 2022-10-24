import importfile as i
import exportfile as e
import view as v
import manual as m

choise = -1
while choise != 'q':
    print('Выбрать действие:\n\t 1. импорт\n\t 2. экспорт\n\t 3. вывод на экран\n\t 4. ручной ввод\n\t q - выход')
    choise = input()

    if choise == '1':
        i.import_file()

    elif choise == '2':
        e.export_file()

    elif choise == '3':
        v.view()

    elif choise == '4':
        m.manual()