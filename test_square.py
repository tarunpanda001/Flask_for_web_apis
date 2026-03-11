from square import get_square

def test_number():
    x = 3
    res = get_square(x)
    assert res == 9
def test_float():
    x = 2.5
    res = get_square(x)
    assert res == 6.25
def test_negative():
    x = -4
    res = get_square(x)
    assert res == 16