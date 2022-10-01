l = []
n = int(input())
for i in range(n):
    l.append(int(input()))

l1 = list(filter(lambda x: x % 7 == 0, l))
if l1 == []:
    print('Числе кратных 7 нет')
else:
    print(l1)
