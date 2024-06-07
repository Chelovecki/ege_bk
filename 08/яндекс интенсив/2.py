from itertools import product

c = 0
for n, r in enumerate(product(sorted('кцичп'), repeat=6), 1):
    if "".join(r).count('и') == 3:
        c += 1
print(c)
