def to_4(n):
    res = ''
    while n != 0:
        res += str(n % 4)
        n //= 4

    return res[::-1]


def f(n):
    a = to_4(n)
    if n % 3 == 0:
        a = list(a)
        a[0], a[-1] = a[-1], a[0]
        a.append('1')
        a = "".join(a)
    else:
        a += str(n % 3)
    return int(a, 4)


print(f(11))
print(f(13))

m = 0
for r in range(11, 100_000):
    res = f(r)
    if res <= 340:
        m = max(m, res)
print(m)
