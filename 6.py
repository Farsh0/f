n = int(input('Введите систему счисления: '))
c = int(input('Введите число: '))
b = ''
while c > 0:
    b = str(c % n) + b
    c = c // n
print(b)
