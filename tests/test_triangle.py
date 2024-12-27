import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area_with_positive_sides(self):
        # Arrange
        side_a = 3
        side_b = 4
        side_c = 5

        # Act
        result = area(side_a, side_b, side_c)

        # Assert
        self.assertEqual(result, 6)  # Площадь треугольника с такими сторонами

    def test_area_with_zero_side(self):
        # Arrange
        side_a = 0
        side_b = 4
        side_c = 5

        # Act
        result = area(side_a, side_b, side_c)

        # Assert
        self.assertEqual(result, 4.5)  # Площадь треугольника с одной стороной равной нулю

    def test_area_with_negative_side_raises_assertion_error(self):
        # Arrange
        side_a = -3
        side_b = 4
        side_c = 5

        # Act & Assert
        with self.assertRaises(AssertionError):
            area(side_a, side_b, side_c)

    def test_perimeter_with_positive_sides(self):
        # Arrange
        side_a = 3
        side_b = 4
        side_c = 5

        # Act
        result = perimeter(side_a, side_b, side_c)

        # Assert
        self.assertEqual(result, 12)  # Периметр треугольника с такими сторонами

    def test_perimeter_with_negative_side_raises_assertion_error(self):
        # Arrange
        side_a = -3
        side_b = 4
        side_c = 5

        # Act & Assert
        with self.assertRaises(AssertionError):
            perimeter(side_a, side_b, side_c)


if __name__ == "__main__":
    unittest.main()
