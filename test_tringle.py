import unittest
from math import sqrt

from Area_calc import check_triangle
from Type_of_triangle import type_finding


class TestOfTriangle(unittest.TestCase):
    def test_values(self):
        self.assertEqual(check_triangle(2, 3, 4), True)
        self.assertEqual(check_triangle(0, 3, 4), False)
        self.assertEqual(check_triangle(2, 0, 4), False)
        self.assertEqual(check_triangle(2, 3, 0), False)
        self.assertEqual(check_triangle(-2, 3, 4), False)
        self.assertEqual(check_triangle(2, -3, 4), False)
        self.assertEqual(check_triangle(2, 3, -4), False)
        self.assertEqual(check_triangle(3, 4, 2), True)
        self.assertEqual(check_triangle(3, 2, 4), True)
        self.assertEqual(check_triangle(2, 3, 4), True)
        self.assertEqual(check_triangle(2, 3, 6), False)
        self.assertEqual(check_triangle(2, 6, 3), False)
        self.assertEqual(check_triangle(2, 3, 5), False)
        self.assertEqual(check_triangle(2, 5, 3), False)
        self.assertEqual(check_triangle(5, 2, 3), False)

    def test_finding_type(self):
        self.assertEqual(type_finding(3, 4, 5), 'Прямоугольный')
        self.assertEqual(type_finding(5, 4, 3), 'Прямоугольный')
        self.assertEqual(type_finding(3, 5, 4), 'Прямоугольный')
        self.assertEqual(type_finding(2, 2, 2), 'Равносторонний')
        self.assertEqual(type_finding(2, 2, 3), 'Равнобедренный')
        self.assertEqual(type_finding(3, 2, 2), 'Равнобедренный')
        self.assertEqual(type_finding(2, 3, 2), 'Равнобедренный')
        self.assertEqual(type_finding(4, 4, 4 * sqrt(2)), 'Равнобедренный')
        self.assertEqual(type_finding(2, 6, 8), 'Обычный')
