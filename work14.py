# написать функцию принимающую последовательность дробных чисел, функция должна возвращать True

def check_float(*args):
    filtered = list(filter(lambda x: x - int(x) > 0.3, args))
    return len(args) == len(filtered)
