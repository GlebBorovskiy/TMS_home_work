#Написать функцию проверяющую тип параметра t и возвращающую число соответствующее типу.  Если тип t это tuple вернуть на 1. Если list вернуть 2. Если str вернуть 3. Если любой другой тип - бросить исключение TypeError.  Если возникло исключение - вывести на экран текст ошибки. Продемонстрировать работу для типов tuple, list, dict, int, str, float
def check_type(t):
    variable_type = type(t)
    if variable_type == tuple: return 1
    elif variable_type == list: return 2
    elif variable_type == str: return 3
    else: raise TypeError()

print(check_type( () ))
print(check_type( [] ))
print(check_type( '' ))
print(check_type( {} ))
print(check_type( 1 ))
print(check_type( 0. ))


