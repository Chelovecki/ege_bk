from itertools import product

for n, r in enumerate(product(sorted('авлос'), repeat=4), 1):
    if r[0] == 'л':
        print(n, "".join(r))
        break
