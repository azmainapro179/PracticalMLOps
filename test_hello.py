from hello import add


def test_add():
    assert 2 == add(1, 1)
    assert 10 == add(7, 3)
    assert 2 == add(4, -2)
    assert -1 == add(-1, 0)
