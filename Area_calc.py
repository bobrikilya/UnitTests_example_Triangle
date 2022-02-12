from math import sqrt


def area_calc(a, b, c):
    p = (a + b + c) / 2
    try:
        return sqrt(p * (p - a) * (p - b) * (p - c))
    except ValueError:
        raise ValueError("Такого треугольника не существует")

# print(area_calc(2, 3, 0))