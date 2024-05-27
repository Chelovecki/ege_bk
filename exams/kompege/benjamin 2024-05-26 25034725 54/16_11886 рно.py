import math


def g(n):
    if n < 10: return n
    if n >= 10: return g(n - 2) + 1


def f(n):
    return g(n - 1)


c = 0
for r in range(1, 100 + 1):
    res = f(r)
    if int(math.sqrt(res)) ** 2 == res and res > 0:
        print(r, res)
        c += 1
print("ответ:", c)
