import itertools


def f(x):
    b = 24 <= x <= 90
    c = 47 <= x <= 115
    a = a1 <= x <= a2

    return c <= (((not a) and b) <= (not c))


ox = [i / 4 for i in range(24 * 4, 115 * 4)]
res = set()
for a1, a2 in itertools.combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        res.add(a2 - a1)
print(min(res))
