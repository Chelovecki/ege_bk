def div(n):
    res = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0 and d != 1:
            res.add(d)
            res.add(n // d)
    return res


for r in range(625681, 758642):
    a = div(r)
    if len(a) == 7:
        if all(delitel > 9 for delitel in a):
            a = sorted(a)
            print(a[-2], a[-1])
