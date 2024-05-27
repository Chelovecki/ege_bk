from functools import lru_cache


@lru_cache(None)
def f(a, b):
    if a > b or a == 100: return 0
    if a == b: return 1
    s = 0

    if a % 10 != 0:
        s += f(a + (a % 10), b)
    if a % 68 != 0:
        s += f(a + (a % 68), b)
    s += f(a ** 2, b)
    return s


a = f(2, 68)
b = f(68, 680)
print(a * b)
