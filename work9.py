#Сгенерировать список из N случайных целых чисел в диапазоне 10000-1000000

import random
def generate_list(n):
    return [random.randint(10000,1000000) for i in range(n)]

 transform_inline(*generate_list(3))

