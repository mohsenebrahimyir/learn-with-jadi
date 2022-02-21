from zarb import zarb

def test_zarb():
    assert zarb(3, 4)  ==  12
    assert zarb(0, 10) ==  0
    assert zarb(-4, 4) == -16
    assert zarb(0, 0)  ==  0