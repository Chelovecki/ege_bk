from itertools import permutations

c = set()
for r in permutations('просто', r=6):
    r = "".join(r)
    if 'оо' not in r:
        c.add(r)
print(len(c))
