from itertools import product

c = 0
for r in product('012345678', repeat=6):
    if r[0] != '0':
        r = int("".join(r))
        if r % 2 == 0:
            r = str(r)
            # for b in '2468':
            #     r=r.replace(b,'0')
            #     if r.count('0') <= 2:
            #         c+=1
            if len([b for b in r if int(b) % 2 == 0]) <= 2:
                c += 1
print(c)
