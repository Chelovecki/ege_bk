from itertools import *

res = set()
for r in product('01234567', repeat=5):
    if r[0] != '0':
        if len(set(r)) == 3 and len([b for b in r if r.count(b) == 3]) == 3:
            if any(r.count(dig) == 3 for dig in '0123456789'):
                res.add(r)
print(len(res))
