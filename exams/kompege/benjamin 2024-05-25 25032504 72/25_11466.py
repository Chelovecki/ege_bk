def div(x):
    res = set()
    for r in range(1, int(x ** 0.5) + 1):
        if x % r == 0:
            if str(r).endswith('9'):
                res.add(r)
                res.add(x // r)
    if res:
        b = min(res)
        if b!=1 and b!=x and b !=9:
            return b

c=0
for r in range(600_001, 10_000_000):
    a = div(r)
    if c==5:
        break
    if a:
        print(r,a)
        c+=1

