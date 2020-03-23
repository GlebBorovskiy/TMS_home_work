#продемонстрировать работу функции из задания 6. входные данные получить из файла input.txt

def check_float(*args):
    filtered = list(filter(lambda x: x - int(x) > 0.3, args))
    return len(args) == len(filtered)

with open('in.txt') as file:
    data = file.read().strip()

print(check_float(*[float(x) for x in data.split(' ')]))

