def to_4(n):
    res = ''
    while n != 0:
        res += str(n % 4)
        n //= 4
    return res[::-1]


def f(n):
    four = to_4(n)
    if n % 3 == 0:
        a, b = four[-1], four[0]
        four = a + four[1:]
        four = four[:-1] + b
        four += '1'
    else:
        four += str(n % 3)
    return int(four, 4)


print(f(11))
print(f(13))
print()
res = []
for n in range(1, 100_000):
    a = f(n)
    if a < 340:
        res.append(a)
print(max(res))
