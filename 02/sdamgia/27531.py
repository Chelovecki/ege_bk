from itertools import *


def f(x, y, z, w):
    return (x <= y) and (y == (not z)) and (z or w)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [
        (1, 1, a1, 1),
        (a2, 1, 1, a3),
        (1, a4, a5, a6)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p, sep='')
