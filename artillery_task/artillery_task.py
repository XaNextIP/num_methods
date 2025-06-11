import math

def xpol(p, angle_rad):
    return p * math.cos(angle_rad)

def ypol(p, angle_rad):
    return p * math.sin(angle_rad)

# Координаты огневой позиции (по умолчанию в начале координат)
x0, y0 = 0, 0

# Ввод координат наблюдательного пункта
xn = int(input("Введите координату xn наблюдательного пункта: "))
yn = int(input("Введите координату yn наблюдательного пункта: "))

# Радиус цели (возможно, под корнем)
if input("Координата P цели стоит под знаком корня? (да/нет): ").strip().lower() == "да":
    pt = math.sqrt(float(input("Введите подкоренное значение радиуса цели: ")))
else:
    pt = float(input("Введите значение радиуса цели: "))

# Угол цели (в градусах)
angle_target_deg = float(input("Введите полярную координату (угол) цели в градусах: "))
angle_target_rad = math.radians(angle_target_deg)

# Переводим цель в декартовые координаты
xt = xpol(pt, angle_target_rad) + xn
yt = ypol(pt, angle_target_rad) + yn

# Вычисляем дальность и угол до цели от огневой позиции (0,0)
dx = xt - x0
dy = yt - y0
distance = math.hypot(dx, dy)
angle_result_rad = math.atan2(dy, dx)
angle_result_deg = math.degrees(angle_result_rad)
if angle_result_deg < 0:
    angle_result_deg += 360

# Вывод
print(f"\nКоординаты цели: x = {xt:.2f}, y = {yt:.2f}")
print(f"Дальность до цели: {distance:.2f}")
print(f"Угол направления на цель: {angle_result_deg:.2f}°")
