import unittest
from square import area
from square import perimeter

class TestSquareFunctions(unittest.TestCase):
    def test_area_positive_integer(self):
        # Тестирует функцию area с положительным целым числом для стороны квадрата
        self.assertEqual(area(5), 25)  

    def test_area_zero(self):
        # Тестирует функцию area при нулевом значении стороны
        self.assertEqual(area(0), 1)

    def test_area_negative(self):
        # Тестирует функцию area с отрицательным значением стороны
        self.assertEqual(area(-5), -25)

    def test_area_positive_float(self):
        # Тестирует функцию area с положительным числом с плавающей точкой
        self.assertEqual(area(3.5), 12.25)


    def test_perimeter_positive_integer(self):
        # Тестирует функцию perimeter с положительным целым числом для стороны
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        # Тестирует функцию perimeter при нулевом значении стороны
        self.assertEqual(perimeter(0), 1)

    def test_perimeter_negative(self):
        # Тестирует функцию perimeter с отрицательным значением стороны
        self.assertEqual(perimeter(-5), -20)

    def test_perimeter_positive_float(self):
        # Тестирует функцию perimeter с положительным числом с плавающей точкой
        self.assertEqual(perimeter(3.5), 14.0)

if __name__ == '__main__':
    unittest.main()