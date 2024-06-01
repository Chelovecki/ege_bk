from itertools import product

for n, r in enumerate(product(sorted('парус'), repeat=5), 1):
    r = "".join(r)
    if r.count('у') <= 1 and 'ау' not in r and 'уа' not in r:
        print(n, r)
