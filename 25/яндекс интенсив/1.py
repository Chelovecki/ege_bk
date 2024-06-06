def div(x):
    res = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0 and d!=14 and str(d).endswith('14'):
            res.add(d)
            res.add(x//d)
    return res

c=0
for r in range(800_000, 1_000_000):
    if c==5:break
    res = div(r)
    if res:
        print(r, min(res))
        c+=1