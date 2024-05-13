from math import gcd


def f2(n, m, k):
    return gcd(n, k) == gcd(m, k)


c = 0
for a in range(1, 1000 + 1):
    if all(f2(a, 420, 2) or ((not (f2(a, x, 12))) <= (not (f2(110, x, 11)))) for x in range(10000)):
        c += 1
print(c)
