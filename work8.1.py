#переписать задание 1 используя цикл

def transform(*args):
    l = []
    for x in args:
        if not (x % 3 == 0 and x % 5 == 0):
            if x % 2 == 0:
                l.append("Even " + str(x) )
            else:l.append( "Odd " + str(x))
    return l


inp = int(input())
r = transform(*range(inp))
print(r)
