def to_5(n: int):
    res = ''
    while n:
        res += str(n % 5)
        n //= 5
    return res[::-1]


def f(n: int):
    five = to_5(n)

    if int(five[-1]) % 2 == 0:
        five += '2'
    else:
        five = f'2{five}3'

    return int(five,5)


print(f"проверка, f(13) = {f(13)}")

print(max([r for r in range(1, 100_000) if f(r)<1000]))
