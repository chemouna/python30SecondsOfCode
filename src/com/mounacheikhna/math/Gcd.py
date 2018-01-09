def gcd(a, b):
    if abs(a) < abs(b):
        gcd(b, a)

    while b > 0:
        q, r = divmod(a, b)
        a, b = b, r

    return a


print gcd(12, 18)
