#Сгенерировать список из N случайных целых чисел в диапазоне 10000-1000000

import datetime
def generate_date_range():
    l = []
    date1 = input()
    date2 = input()
    start = datetime.datetime.strptime(date1, '%d-%m-%Y')
    end = datetime.datetime.strptime(date2, '%d-%m-%Y')
    step = datetime.timedelta(days=1)
    while start <= end:
        l.append(start.strftime('%Y-%m-%d'))
        start += step
    print(l)

