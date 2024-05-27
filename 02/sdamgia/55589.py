from itertools import *


def f1(x, y, z, w):
    return (x <= y) == (w or (not z))


def f2(x, y, z, w):
    return (x <= y) and ((not w) == z)


for a1, a2, a3 in product([0, 1], repeat=3):
    table = [
        (a1, 1, 0, 1),
        (a2, 0, 0, 0),
        (0, a3, 0, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            for f01, f02 in product([0, 1], repeat=2):
                c1 = [f1(**dict(zip(p, r))) for r in table] == [f01, 0, 0]
                c2 = [f2(**dict(zip(p, r))) for r in table] == [0, f02, 1]
                if c1 and c2:
                    print(*p, sep='')
