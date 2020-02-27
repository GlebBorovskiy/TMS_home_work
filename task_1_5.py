import math
a = 3
b = 4
c = math.sqrt(a ** 2 + b ** 2)
print(c)
p = (a + b + c) / 2
s = math.sqrt(p * ((p - a) * (p - b) * (p - c)))
print(s)
