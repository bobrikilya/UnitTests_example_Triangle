def type_finding(a, b, c):
    sides = [a, b, c]
    sides.sort(reverse=True)
    if a == b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    elif sides[0]**2 == sides[1]**2 + sides[2]**2:
        return "Прямоугольный"
    else:
        return "Обычный"

# print(type_finding(3, 4, 5))
