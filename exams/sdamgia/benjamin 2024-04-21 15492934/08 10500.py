from itertools import product

c = 0
for r in product('12345', repeat=5):
    if r.count('1') == 3: c += 1
print(c)
