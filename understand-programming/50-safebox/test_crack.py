from crack import sit


def test_sit():
    assert sit("123", "145") == (1, 0)
    assert sit("123", "142") == (1, 1)
    assert sit("123", "456") == (0, 0)
    assert sit("123", "123") == (3, 0)
