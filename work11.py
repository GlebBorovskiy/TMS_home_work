# Реализовать полную копию функции range с тремя параметрами

def my_range(n, start=0, step=1):
    l = []
    if type(n) != int or type(start) != int or type(step) != int:
        raise TypeError()
    if n < 1:
        return l
    current = start
    while current < n:
        l.append(current)
        current += step
    return l

my_range(5)
my_range(5, start=3)
my_range(5, step=2)
my_range(5, start=3, step=2)


#11. Написать функцию, которая принимает неограниченное количество произвольных параметров по ключу
def create_dict(**kwargs):
    return { value:key for key,value in kwargs.items()}

create_dict(ololo=1, azaza=2)

