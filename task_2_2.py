fib1 = 1
fib2 = 2

n = input ("Номер элемента Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fib_summ = fib1 + fib2
    fib2 = fib_summ
    i = i + 1
print(fib2)
