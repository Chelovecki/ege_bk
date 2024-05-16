from itertools import product

for n, r in enumerate(product(sorted('парус'), repeat=5), 1):
    r = "".join(r)

    if r.count('у') <= 1:
        if 'аа' not in r:
            # if 'а'not in r and 'ааааа' not in r and 'аааа' not in r and 'ааа' not in r and 'aa' not in r:
            print(n, r)
