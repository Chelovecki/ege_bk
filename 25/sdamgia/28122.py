def div(x):
    res = set()
    for r in range(1, int(x ** 0.5) + 1):
        if x % r == 0:
            res.add(r)
            res.add(x // r)
    return res


for r in range(489_421, 489_441):
    a = div(r)
    if len(a) == 4:
        print(sorted(a))
