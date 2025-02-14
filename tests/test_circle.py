import sys
import os
import pytest
from circle import area, perimeter
import math
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


def test_area():
    result = area(5)
    expected_result = math.pi * 5 ** 2
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_perimeter():
    result = perimeter(5)
    expected_result = 2 * math.pi * 5
    assert result == pytest.approx(expected_result, rel=1e-2)


def test_area_invalid():
    with pytest.raises(TypeError):
        area("five")


def test_perimeter_invalid():
    with pytest.raises(TypeError):
        perimeter("five")
