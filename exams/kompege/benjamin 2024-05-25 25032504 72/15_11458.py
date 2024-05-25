def qy(x, y):
    return x & y


def log_(a, x):
    return ((qy(x, 52) != 0) and (qy(x, 36) == 0)) <= (not (qy(x, a) == 0))


for a in range(100):
    if all([log_(a, x) for x in range(10_0000)]):
        print(a)
        break
