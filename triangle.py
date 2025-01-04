def area(a, b, c):
    assert all(x > 0 for x in [a, b, c])

    p = (a + b + c) / 2
    return (
        p * (p - a) * (p - b) * (p - c)
    ) ** 0.5


def perimeter(a, b, c):
    assert all(x > 0 for x in [a, b, c])
    return a + b + c
