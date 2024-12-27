import unittest
from calculate import calculate


class TestCalculate(unittest.TestCase):
    def test_calculate_circle_area(self):
        # Arrange
        figure = "circle"
        function = "area"
        size = [3]

        # Act
        with self.assertRaises(
            NameError
        ):  # circle module is not imported dynamically in `calculate.py`
            calculate(figure, function, size)

    def test_calculate_square_perimeter(self):
        # Arrange
        figure = "square"
        function = "perimeter"
        size = [5]

        # Act
        with self.assertRaises(
            NameError
        ):  # square module is not imported dynamically in `calculate.py`
            calculate(figure, function, size)

    def test_invalid_figure_raises_assertion_error(self):
        # Arrange
        figure = "hexagon"
        function = "area"
        size = [5]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calculate(figure, function, size)

    def test_invalid_function_raises_assertion_error(self):
        # Arrange
        figure = "circle"
        function = "volume"
        size = [3]

        # Act & Assert
        with self.assertRaises(AssertionError):
            calculate(figure, function, size)


if __name__ == "__main__":
    unittest.main()
