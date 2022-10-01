names = ['Маша', 'Петя', 'Вася']

code = list(map(lambda x: hash(x), names))

print(code)
