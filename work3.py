#Написать функцию которая печатает числа от 0 до n, n - параметр. Если число делится на 3, вместо числа печатает fizz, если число делится на 5, вместо числа печатает buzz. Если число делится и на 3 и на 5, вместо числа печатает fizzbuzz

def print_numbers(n):
    for x in range(0, n+1):
        if x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        else:
            print (x)

print_numbers(15)    
