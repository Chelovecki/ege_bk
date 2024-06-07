def to_7(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]


def f(x):
    x_7 = to_7(x)
    if sum([int(r) for r in x_7]) % 2 == 0:
        x_7 += '0'
    else:
        x_7 = '6' + x_7[1:]
    return int(x_7, 7)


res = []
for n in range(1, 100_000):
    r = f(n)
    if r < 119:
        res.append(r)
print(max(res))
