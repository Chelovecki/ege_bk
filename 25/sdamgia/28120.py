def div(x):
    res = set()
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            res |= {d, x // d}
    return sorted(res)


for r in range(201455, 201470 + 1):
    res = div(r)
    if len(res) == 4:
        print(res)
