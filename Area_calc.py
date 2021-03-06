from math import sqrt


def area_calc(a, b, c):
    p = (a + b + c) / 2
    try:
        return sqrt(p * (p - a) * (p - b) * (p - c))
    except ValueError:
        raise ValueError("Такого треугольника не существует")


def check_triangle(a, b, c):
    for i in [a, b, c]:
        if i < 0:
            return False
    p = (a + b + c) / 2
    if p - max(a, b, c) == 0:
        return False
    try:
        sqrt(p * (p - a) * (p - b) * (p - c))
        return True
    except ValueError:
        return False
