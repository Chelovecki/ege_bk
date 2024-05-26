def f(n):
    aye = [int(r) for r in str(n)]
    res1 = aye[0] * aye[1]
    res2 = aye[1] * aye[2]
    res = sorted((res1, res2))
    res = [str(r) for r in res]
    return int("".join(res))


# print(f(631))

for r in range(100, 10_000):
    a = f(r)
    if a == 621:
        print(r)
