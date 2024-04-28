from itertools import *


def f1(x, y, z, w):
    return (x or (not y)) == (z <= w)


def f2(x, y, z, w):
    return ((not x) == y) and (z <= w)


for a1, a2, a3 in product([0, 1], repeat=3):
    table = [
        (a1, 0, 0, 0),
        (0, 0, a2, 0),
        (a3, 1, 1, 0)
    ]

    for val_f1, val_f2 in product([0, 1], repeat=2):
        for p in permutations('xyzw'):
            c1 = [f1(**dict(zip(p, r))) for r in table] == [0, 0, val_f1]
            c2 = [f2(**dict(zip(p, r))) for r in table] == [val_f2, 1, 0]

            if c1 and c2:
                print(*p, sep='')
