l = []
n = int(input('Введите число параметров: '))
for i in range(n):
    l.append(abs(int(input("Введите число: "))))
print('Минимальное значение по модулю: ', min(l))
print('Максимальное значение по модулю: ', max(l))

