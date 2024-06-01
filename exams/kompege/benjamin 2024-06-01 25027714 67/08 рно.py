from itertools import product

c = 0
for r in product('012345678', repeat=6):
    if r[0] != '0':
        if sum([int(b) for b in r]) % 2 == 0:
        # if int("".join(r),9) % 2 == 0:
            r = str(r)
            if r.count('0') + r.count('2') + r.count('4') + r.count('6') + r.count('8') <= 2:
                c += 1

print(c)
