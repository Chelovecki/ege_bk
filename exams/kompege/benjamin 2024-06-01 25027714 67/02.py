from itertools import product, permutations


def f(x, y, z, w):
    return (x or (not y)) and (not (x == z)) and w


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [
        (1, 0, a1, a2),
        (0, 1, 1, a3),
        (a4, a5, 0, a6)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep='')
