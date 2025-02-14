import unittest
from circle import area as area_circle
from circle import perimeter as perimeter_circle

class TestCircleFunctions(unittest.TestCase):

    def test_area_сircle(self):
        # Integer values
        self.assertEqual(area_circle(0), 0)
        self.assertEqual(area_circle(1), 3.14)
        self.assertEqual(area_circle(6), 113.04)
        self.assertEqual(area_circle(20), 1256)
        self.assertEqual(area_circle(102), 32668.56)
        self.assertEqual(area_circle(1237), 4804730.66)
        self.assertEqual(area_circle(23112005), 1677277393876878.5)

        # Double values
        self.assertEqual(area_circle(0.0), 0.0)
        self.assertEqual(area_circle(2.718), 23.2)
        self.assertEqual(area_circle(3.1415), 30.99)
        self.assertEqual(area_circle(22.112004), 1535.27)
        self.assertEqual(area_circle(52.5252), 8662.94)

    def test_perimeter_circle(self):
        # Integer values
        self.assertEqual(perimeter_circle(0), 0)
        self.assertEqual(perimeter_circle(1), 6.28)
        self.assertEqual(perimeter_circle(18), 113.04)
        self.assertEqual(perimeter_circle(100), 628)
        self.assertEqual(perimeter_circle(1337), 8396.36)
        self.assertEqual(perimeter_circle(6072005), 38132191.4)

        # Double values
        self.assertEqual(perimeter_circle(0.0), 0.0)
        self.assertEqual(perimeter_circle(10.19), 63.99)
        self.assertEqual(perimeter_circle(1331.1331), 8359.52)
        self.assertEqual(perimeter_circle(228336.2093), 1433951.39)
        self.assertEqual(perimeter_circle(19249189.11219), 120884907.62)

if __name__ == '__main__':
    unittest.main()
