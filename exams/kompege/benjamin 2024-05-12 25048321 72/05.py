def to_3(n):
    res = ''
    while n != 0:
        res += str(n % 3)
        n //= 3
    return res[::-1]


def f(n):
    t = to_3(n)
    if n % 3 == 0:
        t += t[-2] + t[-1]
    else:
        t += to_3((n % 3) * 5)
    return int(t, 3)


print(f(11))
print(f(12))
print('-' * 30)
res = []
for n in range(1, 100_000):
    a = f(n)
    if a > 133:
        res.append(a)
print(min(res))
