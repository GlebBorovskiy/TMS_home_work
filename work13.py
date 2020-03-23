#реализовать декоратор, который будет печатать параметры переданные в декорируемую функцию


from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        with open('out.txt', 'a+') as file:
            str_args = [str(x) for x in args]
            file.write(' '.join(str_args) + "\n")
        return f(*args, **kwds)
    return wrapper

@my_decorator
def test(a,b,c):
    pass

test(1,2,3)
