import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))

from square_tests import TestSquareFunctions
from rectangle_tests import TestRectangleFunctions
from circle_tests import TestCircleFunctions
from triangle_tests import TestTriangleFunctions

class CustomTestRunner(unittest.TextTestRunner):
    def __init__(self, stream=None, resultclass=None):
        super().__init__(stream=stream, resultclass=resultclass)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestSquareFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestRectangleFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestCircleFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestTriangleFunctions))

    runner = CustomTestRunner()
    runner.run(suite)
