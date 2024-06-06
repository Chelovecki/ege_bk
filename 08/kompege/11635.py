from itertools import product
for r in product(range(9), repeat=27):
    if r[0]!=0:
        print(len(r))