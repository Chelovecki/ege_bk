from itertools import *


def f(x, y, z, w):
    return (not (x <= w)) or (y == z) or y


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [
        (a1, 1, a2, 0),
        (a3, 0, 1, a4),
        (a5, a6, 0, a7)
    ]
    for p in permutations('zyxw'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(*p, sep='')
