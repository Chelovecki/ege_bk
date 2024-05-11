from itertools import *

res = set()
for r in product('01234567', repeat=5):
    if r[0] != '0':
        r = "".join(r)
        if any(b + b + b in r for b in '01234567'):
            if len([b for b in r if r.count(b) == 1]) == 2 and len([b for b in r if r.count(b) == 3]) == 3:
                res.add(r)
print(len(res))


