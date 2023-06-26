# Задача 38: Создать телефонный справочник возможностью добавления 
# записей и чтения. Пользователь также может ввести фамилию, 
# тогда программа должны вывести на экран все записи с этой фамилий. 
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.

def imp():
    surname = input('введите фамилию: ')
    name = input('введите имя: ')
    phone = input('введите телефонный номер: ')

    return surname, name, phone

def controller():
    node = int(input('Выберите режим работы со справочником: (1- найти контакт, 2 - создать контакт)' ))
    if node == 1:
        pass
    elif node == 2:
        dateset = input.dateset()
        write_person(dateset)
    else:
        print(' Такого режима не существует')
        controller()
def write_person(dateset: tuple):
    with open('test.txt', 'a', encoding ='utf-8') as file:
        file.write('\n')
        file.write('\n'.join(dateset))
