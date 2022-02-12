from math import sqrt


def area_calc(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

# print(area_calc(2, 3, 0))
