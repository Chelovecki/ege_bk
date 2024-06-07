from itertools import product, permutations


def f(x, y, z, w):
    return ((w == 1) <= z) and ((not y) and x)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [
        (0, 0, 1, a1),
        (0, 1, 1, 0),
        (a2, a3, 1, 0),
        (0, a4, 1, 0)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0, 1]:
                print(*p, sep='')
