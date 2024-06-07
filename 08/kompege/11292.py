from itertools import product

c = 0
for r in product('0123456789ABCDEF', repeat=5):
    if r[0] != '0' and r.count('6') == 2:
        r = "".join(r)
        for rep in '0248ACE':
            r = r.replace(rep, '0')

        if '06' not in r and '60' not in r and '66' not in r:
            c += 1
print(c)

# главное помнить - что не надо использовать '6' в списке для rep‘
