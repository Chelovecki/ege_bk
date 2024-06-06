from itertools import product

c = 0
for r in product('0123', repeat=4):
    if r[0]!='0':
        r = "".join(r)
        ay = [symb for symb in r if r.count(symb) >= 2]
        if len(ay) > 0:
            c += 1
print(c)
