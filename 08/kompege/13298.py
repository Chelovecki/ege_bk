from itertools import product

res = []
for n, r in enumerate(product(sorted('привычка'), repeat=5), 1):
    if n % 5 != 0:
        res.append("".join(r))

c = 0
for r in res:
    c += 1
    if 'и' not in r and 'ы' not in r and 'а' not in r:
        if len(r) == len(set(r)):
            print(c)
            break
