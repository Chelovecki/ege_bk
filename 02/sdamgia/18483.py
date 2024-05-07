from itertools import *


def f(x, y, z, w):
    return ((y <= w) == (x <= (not z))) and (x or w)


for a1, a2 in product([0, 1], repeat=2):
    table = [
        (0, 1, 1, 1),
        (1, 0, 1, 0),
        (a1, 0, 0, a2)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 1, 1]:
                print(*p, sep='')