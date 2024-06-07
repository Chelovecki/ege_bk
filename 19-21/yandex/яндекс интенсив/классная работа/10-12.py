import math


def f(s1, s2, m):
    if s1 + s2 <= 20: return m % 2 == 0
    if m == 0 or s1 < 0 or s2 < 0: return 0
    h = [
        f(math.ceil(s1 / 2), s2, m - 1),
        f(s1, math.ceil(s2 / 2), m - 1),
        f(s1 - 1, s2, m - 1),
        f(s1, s2 - 1, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [r for r in range(11, 500) if f(10, r, 2)])
print('20)', [r for r in range(11, 500) if not f(10, r, 1) and f(10, r, 3)])
print('21)', [r for r in range(11, 500) if not f(10, r, 2) and f(10, r, 4)])
