from itertools import product, permutations


def f(x, y, z, w):
    return (not x <= (not z <= w)) and ((not z) <= ((not w) == y))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    t = [
        (1, a1, 1, 1),
        (a2, a3, 0, 0),
        (a4, 0, 0, a5)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 1, 1]:
                print(*p, sep='')
