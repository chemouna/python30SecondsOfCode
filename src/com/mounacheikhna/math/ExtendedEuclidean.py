
def extendedEuclidean(a, b):
    if abs(a) < abs(b):
        (x, y, d) = extendedEuclidean(b, a)
        return y, x, d

    