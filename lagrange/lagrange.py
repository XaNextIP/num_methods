import numpy as np
import matplotlib.pyplot as plt

# Интерполяция Лагранжа
def lagrange_interpolate(x_values, y_values, target_x):
    result = 0
    for j in range(len(y_values)):
        numerator = 1
        denominator = 1
        for i in range(len(x_values)):
            if i == j:
                continue
            numerator *= (target_x - x_values[i])
            denominator *= (x_values[j] - x_values[i])
        result += y_values[j] * (numerator / denominator)
    return result

# Ввод
n = int(input("Количество аргументов: "))
print("Введите координаты xi и соответствующие ti:")

times = []
values = []

for i in range(n):
    val = float(input(f"Значение xi [{i+1}]: "))
    t = float(input(f"Значение ti [{i+1}]: "))
    values.append(val)
    times.append(t)

# Интерполяция
xnew = np.linspace(min(times), max(times), 100)
ynew = [lagrange_interpolate(times, values, tx) for tx in xnew]

# Визуализация
plt.plot(times, values, 'o', label='Исходные точки')
plt.plot(xnew, ynew, '-', label='Интерполяция Лагранжа')
plt.title('Интерполяция полиномом Лагранжа')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()
