from Type_of_triangle import type_finding
from Area_calc import area_calc
from Area_calc import check_triangle


def main():
    a = float(input("Введите a грань: "))
    b = float(input("Введите b грань: "))
    c = float(input("Введите c грань: "))
    # print(area_calc(a, b, c))
    # print(type_finding(a, b, c))
    print(check_triangle(a, b, c))


if __name__ == '__main__':
    main()
