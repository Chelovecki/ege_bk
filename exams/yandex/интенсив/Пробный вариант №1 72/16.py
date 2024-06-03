from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1000: return n ** (n ** 2)
    return n + (2 * f(n - 2)) + (6 * f(n - 6))


for r in range(20_024):
    f(r)
    print(r)
print(f(20_024)) - 2 * f(20_022) - 3 * f(20_020) + 18 * f(20_014)
