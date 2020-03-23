# Реализовать функцию принимающую последовательность целых чисел и возвращающую сумму нечетных чисел 

import functools
def reduce_to_odd_sum(*args):
    return functools.reduce(lambda a, b: a + b if b%2!=0  else a, args)

reduce_to_odd_sum(1,2,3,4,5,6,7,8)

