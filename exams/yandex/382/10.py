from itertools import product

res = set()
for r in product('яндекс', repeat=5):
    if r[0] not in 'ндкс' and r.count('я') + r.count('е') == 2:
        res.add("".join(r))
print(len(res))