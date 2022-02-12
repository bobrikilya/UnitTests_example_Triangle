import unittest
from Area_calc import check_triangle


class TestOfTriangle(unittest.TestCase):
    def test_value(self):
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


