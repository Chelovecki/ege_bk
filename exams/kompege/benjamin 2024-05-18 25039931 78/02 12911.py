from itertools import permutations


def f(x, y, z):
    return (not (z) and x) or (x and y)


t = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

for p in permutations('xyz'):
    if [f(**dict(zip(p, r))) for r in t] == [0, 1, 0, 1, 0, 0, 0, 1]:
        print(*p, sep='')
