from itertools import product

c = 0
for r in product('0123456789', repeat=6):
    o += 1
    if r[0] != '0':
        if int("".join(r)) % 5 == 0 and len(r) == len(set(r)):
            r = "".join(r)
            for b in '02468':
                r = r.replace(b, '0')
            for b in '13579':
                r = r.replace(b, '1')

            if '11' not in r and '00' not in r:
                c += 1

print(c)
