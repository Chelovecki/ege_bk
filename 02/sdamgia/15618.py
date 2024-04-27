# https://inf-ege.sdamgia.ru/problem?id=15618
from itertools import *


def f(x, y, z, w):
    return (x and (not y)) or y == z or (not w)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = set([
        (a1, 0, a2, a3),
        (1, 0, a4, 0),
        (1, a5, 0, 0)

    ])
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(*p, sep='')