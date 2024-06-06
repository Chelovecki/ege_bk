from itertools import product

c = 0
for r in product('0123456', repeat=6):
    if r[0] != '0':
        r = "".join(r)
        if r.count('0') == 1:
            if len([b for b in r if int(b) % 2 == 0]) % 2 == 0:
                c += 1
print(c)
