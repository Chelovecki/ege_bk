from itertools import product

c = 0
for r in product('0123456789ABC', repeat=6):
    if r[0] != '0' and r.count('5') <= 1:
        r = "".join(r)
        for rep in '13579BD':
            r = r.replace(rep, '1')
        if '11' not in r:
            c += 1
print(c)
