l = []

n = int(input("Число переменных: "))
for i in range(n):
    l.append(int(input("Число: ")))
    
l1 = list(map(lambda x: x % 7, l))
print(f'Остаток списка {l} деленного на 7: ', l1)

