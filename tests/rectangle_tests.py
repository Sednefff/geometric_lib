import unittest
from rectangle import area as area_rectangle
from rectangle import perimeter as perimeter_rectangle

class TestRectangleFunctions(unittest.TestCase):
    def test_area_rectangle(self):
        #Integer values
        self.assertEqual(area_rectangle(0, 0), 0)
        self.assertEqual(area_rectangle(1, 2), 2)
        self.assertEqual(area_rectangle(5, 3), 15)
        self.assertEqual(area_rectangle(6, 0), 0)
        self.assertEqual(area_rectangle(17, 17), 289)
        self.assertEqual(area_rectangle(52, 25), 1300)
        self.assertEqual(area_rectangle(100, 100), 10000)
        self.assertEqual(area_rectangle(123, 321), 39483)

        #Double values
        self.assertEqual(area_rectangle(1.1, 2.31), 2.54)
        self.assertEqual(area_rectangle(38.15, 16.88), 643.97)
        self.assertEqual(area_rectangle(52.5252, 25.2525), 1326.39)
        self.assertEqual(area_rectangle(100.001, 0.0), 0.0)
        self.assertEqual(area_rectangle(18249.12847, 821.12142), 14984750.28)
        
    def test_perimeter_rectangle(self):
        #Integer values
        self.assertEqual(perimeter_rectangle(1, 2), 6)
        self.assertEqual(perimeter_rectangle(5, 10), 30)
        self.assertEqual(perimeter_rectangle(20, 200), 440)
        self.assertEqual(perimeter_rectangle(1092, 10123), 22430)
        self.assertEqual(perimeter_rectangle(19241, 21948), 82378)
        self.assertEqual(perimeter_rectangle(1929318381, 912139139), 5682915040)

        #Double values
        self.assertEqual(perimeter_rectangle(0.0, 1.0), 2.0)
        self.assertEqual(perimeter_rectangle(10.19, 19.10), 58.58)
        self.assertEqual(perimeter_rectangle(1331.1331, 1331.1331), 5324.53)
        self.assertEqual(perimeter_rectangle(1984.1093, 10932.10393), 25832.43)
        self.assertEqual(perimeter_rectangle(2194292.97264, 9102873.12482), 22594332.19)
        
if __name__ == '__main__':
    unittest.main()
