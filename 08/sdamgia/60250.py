from itertools import product

c = 0
for r in product('01234567', repeat=5):
    if r[0] != '0':
        if r.count('1') == 0:
            if len(r) == len(set(r)):
                r = "".join(r)
                for symb in '0246':
                    r = r.replace(symb, '2')
                for symb in '1357':
                    r = r.replace(symb, '1')
                if '11' not in r and '22' not in r:
                    c += 1
print(c)
