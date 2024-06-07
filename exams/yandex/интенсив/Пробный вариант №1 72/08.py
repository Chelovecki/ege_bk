from itertools import product

for n, r in enumerate(product(sorted('июнь'), repeat=5), 1):
    r = "".join(r)
    if r.count('и') + r.count('ю') == 2:
        print(n, r)
