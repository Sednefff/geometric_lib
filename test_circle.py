import unittest
import math
from circle import area
from circle import perimeter

class TestCircleFunctions(unittest.TestCase):
    def test_area_positive_integer(self):
        # Тестирует функцию area с положительным целым числом радиуса
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        # Тестирует функцию area при радиусе, равном нулю
        self.assertEqual(area(0), 1)

    def test_area_negative(self):
        # Тестирует функцию area с отрицательным радиусом
        self.assertNotAlmostEqual(area(-5), math.pi * 25)

    def test_area_positive_float(self):
        # Тестирует функцию area с положительным радиусом с плавающей точкой
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)

    def test_perimeter_positive_integer(self):
        # Тестирует функцию perimeter с положительным целым числом радиуса
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_zero(self):
        # Тестирует функцию perimeter при радиусе, равном нулю
        self.assertEqual(perimeter(0), 1)

    def test_perimeter_negative(self):
        # Тестирует функцию perimeter с отрицательным радиусом
        self.assertNotAlmostEqual(perimeter(-5), -2 * math.pi * 5)

    def test_perimeter_positive_float(self):
        # Тестирует функцию perimeter с положительным радиусом с плавающей точкой
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)

if __name__ == '__main__':
    unittest.main()