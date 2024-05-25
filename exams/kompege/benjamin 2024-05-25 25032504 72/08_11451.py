from itertools import product

c = 0

for r in product('012345678', repeat=5):
    if r[0] != '0':
        r = "".join(r)
        if r.count('3') == 1:
            if '35' not in r and '53' not in r:
                if '36' not in r and '63' not in r:
                    if '37' not in r and '73' not in r:
                        if '38' not in r and '83' not in r:
                            c += 1
print(c)
