def zarb(a, b):
    x = 0
    for i in range(abs(a)):
        if a > 0:
            x += b
        else:
            x -= b

    return x
