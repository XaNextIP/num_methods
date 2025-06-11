import math
import cmath

print("Введите значения коэффициентов A, B и C")
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Все действительные числа являются корнями")
        else:
            print("Нет корней")
    else:
        x = -c / b
        print(f"Линейное уравнение: один корень X = {x}")
else:
    d = b ** 2 - 4 * a * c
    print(f"Дискриминант D = {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Два действительных корня: X1 = {x1}, X2 = {x2}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Один действительный корень: X = {x}")
    else:
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        print(f"Комплексные корни: X1 = {x1}, X2 = {x2}")
