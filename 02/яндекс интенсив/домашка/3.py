from itertools import product, permutations


def f(x, y, w, z):
    return not (w <= x) or (y <= z) or (not y)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    t = [
        (0, 1, a1, a2),
        (a3, 0, a4, 1),
        (a5, a6, a7, 0)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xzyw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(*p, sep='')
