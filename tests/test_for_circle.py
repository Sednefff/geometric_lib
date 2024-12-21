import sys
from circle import area, perimeter
import pytest
sys.path.append('../../geometric_lib/')


@pytest.mark.parametrize("given, when, then", [
    ("3", "area({})", "28.3"),
    ("4", "perimeter({})", "25.1"),
    ("5", "area({})", "78.5"),
    ("6", "perimeter({})", "37.7")
])
def test_circle(given, when, then):
    # Given: подготовка данных
    a = int(given)
    # When: выполнение действия
    result = round(eval(when.format(a)), 1)
    # Then: проверка результата
    assert result == float(then)
