import itertools

a = '02468'
b = ["".join(r) for r in itertools.product('13589', repeat=4)]
b.append('')
poss = []
for x in a:
    for y in b:
        res = f"1{x}2157{y}4"
        poss.append(res)
for r in range(133, 10 ** 10, 133):
    if str(r) in poss:
        print(r, r // 133)
