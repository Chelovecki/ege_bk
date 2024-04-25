def div(x):
    res = set()
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            res.add((x // d) - d)
    return res


for r in range(1_000_000, 2_000_000 + 1):
    res = div(r)
    if len([r for r in res if r <= 100]) >= 3:
        print(r)
