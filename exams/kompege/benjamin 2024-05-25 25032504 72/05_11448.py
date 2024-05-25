def to_3(n):
    res = ''
    while n != 0:
        res += str(n % 3)
        n //= 3
    return res[::-1]


def f(n):
    t = to_3(n)
    if n % 2 == 0:
        t = '1' + t + '00'
    else:
        t += to_3(sum([int(r) for r in t]))
    return int(t, 3)


# print(f(4))
# print(f(7))

for n in range(1, 1000):
    if f(n) > 168:
        print(n)
        break
