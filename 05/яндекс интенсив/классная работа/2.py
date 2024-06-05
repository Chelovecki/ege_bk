def to_7(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]


def f(n):
    s = to_7(n)
    if s.count('2') % 2 == 0:
        s += '555'
    else:
        s = '1' + s
    return int(s, 7)


print(f(11))
print(f(14))

for r in range(1, 100_000):
    if f(r) < 3799:
        print(r)
