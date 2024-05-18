from itertools import permutations

c = 0

for r in permutations('просто'):
    r = "".join(r)
    if 'пп' not in r and 'рр' not in r and 'оо' not in r and 'сс' not in r and 'тт' not in r:
        c += 1
print(c)
