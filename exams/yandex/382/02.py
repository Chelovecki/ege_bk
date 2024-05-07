from itertools import *


def f(x, y, z, w):
    return (z <= x or y) <= x and z and (not w)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (a1, 0, 0, 0),
        (1, 1, 1, a2),
        (a3, 1, a4, a5)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p, sep='')
