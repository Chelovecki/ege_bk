from itertools import product, permutations


def f(x, y, w):
    return (x <= y) and (w or (not w))


for a1, a2, a3 in product([0, 1], repeat=3):
    t = [
        (1, 1, 0),
        (a1, 1, a2),
        (1, 0, 1),
        (1, a3, 1)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xyw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1]:
                print(*p, sep='')
