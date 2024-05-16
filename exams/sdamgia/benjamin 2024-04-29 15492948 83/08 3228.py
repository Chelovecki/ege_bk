from itertools import product

for n, r in enumerate(product('АОУ', repeat=5), 1):
    r = "".join(r)
    if r == 'УАУАУ':
        print(n, r)
