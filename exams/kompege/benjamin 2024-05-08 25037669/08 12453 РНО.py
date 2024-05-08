from itertools import permutations


def l(s: str):
    for r in 'оеь': s = s.replace(r, 'о')
    for r in 'свт': s = s.replace(r, 'с')
    if not ('сс' in s and 'оо' in s):
        return 1
    return 0


c = 0
total_ways = 0

for r in set(permutations('совесть')):
    total_ways += 1
    r = "".join(r)
    c += l(r)

print(c, total_ways)
