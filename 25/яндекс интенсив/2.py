def d(x):
    res = set()
    for r in range(1, int(x ** 0.5) + 1):
        if r % 2 == 0 and x % r == 0:
            res.add(r)
            if x // r % 2 == 0:
                res.add(x // r)
    return res


for r in range(977004, 977022 + 1):
    res = d(r)
    if len(res) >= 6:
        print(r, max(res))
