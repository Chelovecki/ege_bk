from itertools import product

c = 0
for r in product('01234567', repeat=7):
    if r[0] != '0':
        r = "".join(r)
        if sum(symb in '0246' for symb in r) == 2:
            a = ['17', '37', '57', '77', '71', '73', '75']
            if all(b not in r for b in a):
                c += 1
print(c)
