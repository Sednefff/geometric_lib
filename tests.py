import unittest
from tabulate import tabulate

def rectangle_area(a, b): 
    return a * b 

def triangle_area(a, h): 
    return a * h / 2 

def hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

class RectangleTestCase(unittest.TestCase):
    results = []

    def add_result(self, test_name, inputs, expected, actual):
        self.results.append([test_name, inputs, expected, actual, "Passed" if expected == actual else "Not passed"])

    def test_zero_area_rect(self):
        inputs = (10000000, 0)
        expected = 0
        actual = rectangle_area(*inputs)
        self.add_result("test_zero_area_rect", inputs, expected, actual)

    def test_square_area_rect(self):
        inputs = (5, 5)
        expected = 25
        actual = rectangle_area(*inputs)
        self.add_result("test_square_area_rect", inputs, expected, actual)

    def test_big_square_area_rect(self):
        inputs = (13428765983984678, 13428765983984678)
        expected = 180331755852623977151186538763684
        actual = rectangle_area(*inputs)
        self.add_result("test_big_square_area_rect", inputs, expected, actual)

    def test_normal_numbers1_area_rect(self):
        inputs = (120, 100)
        expected = 12000
        actual = rectangle_area(*inputs)
        self.add_result("test_normal_numbers1_area_rect", inputs, expected, actual)
    
    def test_normal_numbers2_area_rect(self):
        inputs = (123456, 234567)
        expected = 28958703552
        actual = rectangle_area(*inputs)
        self.add_result("test_normal_numbers2_area_rect", inputs, expected, actual)

    def test_big_numbers_area_rect(self):
        inputs = (340587394587340, 908623498)
        expected = 309465709844655137315320
        actual = rectangle_area(*inputs)
        self.add_result("test_big_numbers_area_rect", inputs, expected, actual)
    
    def test_zero_area_tr(self):
        inputs = (10000000, 0)
        expected = 0.0
        actual = triangle_area(*inputs)
        self.add_result("test_zero_area_tr", inputs, expected, actual)

    def test_normal_numbers1_area_tr(self):
        inputs = (120, 100)
        expected = 6000.0
        actual = triangle_area(*inputs)
        self.add_result("test_normal_numbers1_area_tr", inputs, expected, actual)
    
    def test_normal_numbers2_area_tr(self):
        inputs = (123456, 234567)
        expected = 14479351776.0
        actual = triangle_area(*inputs)
        self.add_result("test_normal_numbers2_area_tr", inputs, expected, actual)

    def test_big_numbers_area_tr(self):
        inputs = (34058739, 908623)
        expected = 15473276803198.5
        actual = triangle_area(*inputs)
        self.add_result("test_big_numbers_area_tr", inputs, expected, actual)

    def test_zero_hyp(self):
        inputs = (10000000, 0)
        expected = 10000000.0
        actual = hypotenuse(*inputs)
        self.add_result("test_zero_hyp", inputs, expected, actual)
    
    def test_normal_numbers1_hyp(self):
        inputs = (120, 160)
        expected = 200.0
        actual = hypotenuse(*inputs)
        self.add_result("test_normal_numbers1_hyp", inputs, expected, actual)

    def test_normal_numbers2_area_tr(self):
        inputs = (12012, 1602)
        expected = 12118.355829071863
        actual = hypotenuse(*inputs)
        self.add_result("test_normal_numbers2_hyp", inputs, expected, actual)

    def test_big_numbers_hyp(self):
        inputs = (34058739, 908623)
        expected = 34070857.01925107
        actual = hypotenuse(*inputs)
        self.add_result("test_big_numbers_hyp", inputs, expected, actual)
    
    @classmethod
    def tearDownClass(cls):
        print(tabulate(cls.results, headers=["Test's name", "Input", "Expected answer", "Actual answer", "Status"], tablefmt="grid"))
    
if __name__ == '__main__':
    unittest.main()