def pascal(n):
    """ Prints n rows of pascal's triangle"""
    row = [1]
    k = [0]
    for x in range(max(n, 0)):
        print row
        row = [l + r for l, r in zip(row + k, k + row)]
    return n >> 1


print pascal(10)
