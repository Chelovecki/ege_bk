from itertools import product, permutations


def f(x, y, z, w):
    return (x or ((not z) and w) or w) == (y and (not x) and w)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [
        (1, a1, a2, 0),
        (1, a3, 0, 0),
        (0, 1, a4, 1)
    ]

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep="")
