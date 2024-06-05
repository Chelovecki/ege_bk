def to_4(n):
    res = ''
    while n != 0:
        res += str(n % 4)
        n //= 4
    return res[::-1]


def f(n):
    s = to_4(n)
    if n % 3 == 0:
        s = list(s)
        s[0], s[-1] = s[-1], s[0]
        s.append('1')
        s = "".join(s)
    else:
        s += str(n % 3)
    return int(s, 4)


m = 0
for r in range(1, 100_000):
    res = f(r)
    if res <= 340:
        m = max(m, res)
print(m)
