from itertools import product, permutations


def f(x, y, w, u):
    return (not (((y <= w) == x))) and u


for a1, a2, a3 in product([0, 1], repeat=3):
    t = [
        (0, 1, 0, a1),
        (0, 1, 1, 1),
        (1, 0, 1, a2),
        (1, a3, 1, 1)
    ]
    if len(t) == len(set(t)):
        for p in permutations('xywu'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 1, 1]:
                print(*p, sep='')
