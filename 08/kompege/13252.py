from itertools import permutations

c = 0
for r in set(permutations('кидала', 5)):
    r = "".join(r)
    if all(b + b not in r for b in set('кидала')):
        c += 1
print(c)
