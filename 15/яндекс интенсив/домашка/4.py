def f(a, x):
    res = ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))
    return res


for a in range(1, 1000):
    if all(not f(a, x) for x in range(10_000)):
        print(a)
        break
