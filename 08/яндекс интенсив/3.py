from itertools import product

c = 0
for n, r in enumerate(product(sorted('универст'), repeat=6), 1):
    r = "".join(r)
    # print(r)
    for glas in 'уи':
        r = r.replace(glas, 'е')
    # print(r)
    # input()
    if r[0] in 'нврст' and 'еее' in r:
        print(n, r)
