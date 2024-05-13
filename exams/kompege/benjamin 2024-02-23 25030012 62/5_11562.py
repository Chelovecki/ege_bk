def to6(n):
    res = ''
    while n != 0:
        res += str(n % 6)
        n //= 6
    return res[::-1]


def f(n: int):
    number = to6(n)
    if n % 3 == 0:
        number = number[:2] + number
    else:
        number += to6((n % 3) * 10)
    return int(number, 6)


print(f(11))
print(f(12))

for n in range(1, 100_000):
    if f(n) > 680:
        print(f(n))
        break
