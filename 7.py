import sympy

n = int(input("Введите число: "))
if sympy.isprime(n):
    print(f"Число {n} простое")
else:
    print(f"Число {n} не простое")
