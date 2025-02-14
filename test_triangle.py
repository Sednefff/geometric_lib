import unittest
from triangle import area
from triangle import perimeter

class TestTriangleFunctions(unittest.TestCase):
    def test_area_positive_integers(self):
        # Тестирует функцию area с положительными целыми числами для основания и высоты
        self.assertEqual(area(3, 4), 6)

    def test_area_zero(self):
        # Тестирует функцию area при нулевом значении основания или высоты
        self.assertNotEqual(area(0, 10), 1)

    def test_area_negative(self):
        # Тестирует функцию area с отрицательным значением основания или высоты
        self.assertEqual(area(-5, 10), -25)

    def test_area_positive_floats(self):
        # Тестирует функцию area с положительными числами с плавающей точкой для основания и высоты
        self.assertEqual(area(2.5, 4.0), 5.0)


    def test_perimeter_positive_integers(self):
        # Тестирует функцию perimeter с положительными целыми числами для сторон
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        # Тестирует функцию perimeter при нулевом значении одной из сторон
        self.assertNotEqual(perimeter(0, 4, 5), 0) 

    def test_perimeter_negative(self):
        # Тестирует функцию perimeter с отрицательным значением стороны
        self.assertNotEqual(perimeter(-3, 4, 5), 6)

    def test_perimeter_positive_floats(self):
        # Тестирует функцию perimeter с положительными числами с плавающей точкой для сторон
        self.assertEqual(perimeter(2.5, 3.5, 4.0), 10.0)

if __name__ == '__main__':
    unittest.main()