import sys
from square import area, perimeter
import pytest
sys.path.append('../../gg/')


@pytest.mark.parametrize("given, when, then", [
    ("3", "area({})", "9"),
    ("4", "perimeter({})", "16"),
    ("5", "area({})", "25"),
    ("6", "perimeter({})", "24")
])
def test_square(given, when, then):
    # Given: подготовка данных
    a = int(given)
    # When: выполнение действия
    result = round(eval(when.format(a)), 1)
    # Then: проверка результата
    assert result == float(then)
