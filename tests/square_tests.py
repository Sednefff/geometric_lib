import unittest
from square import area as area_square
from square import perimeter as perimeter_square

class TestSquareFunctions(unittest.TestCase):

    def test_area_square(self):
        # Integer values
        self.assertEqual(area_square(0), 0)
        self.assertEqual(area_square(1), 1)
        self.assertEqual(area_square(5), 25)
        self.assertEqual(area_square(9), 81)
        self.assertEqual(area_square(11), 121)
        self.assertEqual(area_square(52), 2704)
        self.assertEqual(area_square(100), 10000)
        self.assertEqual(area_square(333), 110889)
        self.assertEqual(area_square(1237), 1530169)
        self.assertEqual(area_square(14871), 221146641)

        # Double values
        self.assertEqual(area_square(1.1), 1.21)
        self.assertEqual(area_square(38.15), 1455.42)
        self.assertEqual(area_square(38.9), 1513.21)
        self.assertEqual(area_square(52.5252), 2758.9)
        self.assertEqual(area_square(100.001), 10000.2)
        self.assertEqual(area_square(10.29813813), 106.05)

    def test_perimeter_square(self):
        # Integer values
        self.assertEqual(perimeter_square(0), 0)
        self.assertEqual(perimeter_square(1), 4)
        self.assertEqual(perimeter_square(2), 8)
        self.assertEqual(perimeter_square(100), 400)
        self.assertEqual(perimeter_square(19241), 76964)
        self.assertEqual(perimeter_square(111111111111111), 444444444444444)

        # Double values
        self.assertEqual(perimeter_square(0.0), 0.0)
        self.assertEqual(perimeter_square(10.19), 40.76)
        self.assertEqual(perimeter_square(1331.1331), 5324.53)
        self.assertEqual(perimeter_square(1984.02022022), 7936.08)
        self.assertEqual(perimeter_square(19249189.112196794570), 76996756.45)

if __name__ == '__main__':
    unittest.main()
