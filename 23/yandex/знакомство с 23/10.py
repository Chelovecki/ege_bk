from functools import lru_cache


@lru_cache(None)
def f(a, b):
    if a > b or a == 50: return 0
    if a == b: return 1
    c = a + 1
    while c % 3 != 0:
        c += 1
    f1 = f(a + 3, b)
    f2 = f((2 * a) + 1, b)
    f3 = f(c, b)
    return f1 + f2 + f3


print(f(5, 23) * f(23, 89))
