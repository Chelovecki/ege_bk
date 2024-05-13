from functools import lru_cache


@lru_cache(None)
def f(a, b, c_a=0):
    if a > b or c_a > 2: return 0
    if a == b and c_a <= 2:
        return 1
    return f(a - 2, b, c_a + 1) + f(a * 2, b, c_a) + f(a * 3, b, c_a)


for r in range(10, 48):
    f(6, r)
print(f(6, 48))
