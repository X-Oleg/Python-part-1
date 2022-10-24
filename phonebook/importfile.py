rfile = None

def import_file():
    global rfile
    with open('phone.txt', 'r', encoding='utf-8') as file:
        rfile = file.readlines()

    with open('phonebook.txt', 'a', encoding='utf-8') as bd:
        bd.writelines('\n')
        bd.writelines(rfile)
    return rfile