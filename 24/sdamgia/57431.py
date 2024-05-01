import itertools

s = open('57431.txt').read()
poss_repeat = ["".join(r) for r in itertools.product('ABC', repeat=2)]
for r in poss_repeat:
    s = s.replace(r, ' ')

print(max(len(r) for r in s.split()))

#todo