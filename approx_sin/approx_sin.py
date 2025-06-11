import math

# Ввод
x_deg = float(input("Введите аргумент функции sin в градусах: "))
eps = float(input("Введите точность (например, 0.0001): "))
if eps <= 0:
    print("Точность должна быть положительной, меняю знак.")
    eps = abs(eps)

# Перевод в радианы
x_rad = math.radians(x_deg % 360)

# Для сравнения
true_sin = math.sin(x_rad)
print(f"Синус, посчитанный Python'ом = {true_sin:.10f}")

# Инициализация переменных
term = x_rad           # Первое слагаемое ряда
approx_sin = 0.0       # Сумма ряда
n = 0                  # Номер члена

# Итерация по ряду Тейлора
while abs(term) > eps:
    approx_sin += term
    n += 1
    term *= -1 * x_rad ** 2 / ((2 * n) * (2 * n + 1))

# Результаты
print(f"Синус, полученный программой = {approx_sin:.10f}")
print(f"Абсолютная погрешность = {abs(true_sin - approx_sin):.10e}")
