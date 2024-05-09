from itertools import *

c = 0
for r in product(range(12), repeat=7):
    if r[0] != 0:
        if r.count(11) == 2:
            if all(r[idx - 1] % 2 != r[idx] % 2 for idx in range(1, 7)):
                c += 1
print(c)
