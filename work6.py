#Написать функцию, подсчитывающую сколько раз пользователь ввел каждую строку. Пользователь вводить одну строку за раз. Каждый раз счетчик ввода этой строки увеличивается на 1. Если пользователь ввел строку "exit", программа завершается и выводит статистику введенных строк. Счетчики хранить в dict
def string_counter():
    d = {}
    while True:
        new_string = input()
        if new_string != 'exit':
            if new_string in d:
                d[new_string] = d[new_string] + 1
            else:
                d[new_string] = 1
        else:
            print('collecting stats')
            print('stats: ', d)
            return

string_counter()
