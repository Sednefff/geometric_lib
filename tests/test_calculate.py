import sys
import os
import pytest
from calculate import calc, circle, square, triangle  # noqa: F401


sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_circle_area():
    result = calc('circle', 'area', [5])
    expected_result = 3.141592653589793 * 5 ** 2
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_circle_perimeter():
    result = calc('circle', 'perimeter', [5])
    expected_result = 2 * 3.141592653589793 * 5
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_square_area():
    result = calc('square', 'area', [3])
    expected_result = 3 ** 2
    assert result == expected_result


def test_square_perimeter():
    result = calc('square', 'perimeter', [3])
    expected_result = 3 * 4
    assert result == expected_result


def test_triangle_area():
    result = calc('triangle', 'area', [3, 4, 5])
    s = (3 + 4 + 5) / 2
    expected_result = (s * (s - 3) * (s - 4) * (s - 5)) ** 0.5
    assert result == expected_result


def test_triangle_perimeter():
    result = calc('triangle', 'perimeter', [3, 4, 5])
    expected_result = 3 + 4 + 5
    assert result == expected_result


def test_invalid_figure():
    with pytest.raises(AssertionError, match="Invalid figure"):
        calc('trapezoid', 'area', [5])


def test_invalid_function():
    with pytest.raises(AssertionError, match="Invalid function"):
        calc('circle', 'volume', [5])


def test_invalid_size_circle():
    with pytest.raises(AssertionError, match=(
            "Invalid number of parameters for area of circle")):
        calc('circle', 'area', [5, 52])


def test_invalid_size_triangle():
    with pytest.raises(AssertionError, match=(
            "Invalid number of parameters for area of triangle")):
        calc('triangle', 'area', [1, 52])


def test_invalid_size_square():
    with pytest.raises(AssertionError, match=(
            "Invalid number of parameters for area of circle")):
        calc('circle', 'area', [3, 52])
