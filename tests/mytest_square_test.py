# import math.sqrt

def square(x):
    return x * x


def test_squaring_values():
    # Test squaring positive numbers
    assert square(2) == 4
    assert square(3) == 9

    # Test squaring negative numbers
    assert square(-2) == 4
    assert square(-3) == 9

    # Test squaring zero
    assert square(0) == 0

