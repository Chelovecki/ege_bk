from itertools import product

c = 0
for r in product('012345', repeat=6):
    if r[0]!='0':
        r = "".join(r)
        if r.count('2') == 1:
            r = r.replace('3', '1').replace('5', '1')
            if '21' not in r and '12' not in r:
                c += 1
print(c)
