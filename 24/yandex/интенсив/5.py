import itertools

s = open('5.txt').read()
# print(list(["".join(r) for r in itertools.product('ABC', repeat=2)]))
restricted = ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']

c = m = 1
for r in range(1, len(s)):
    ay = s[r - 1] + s[r]
    if ay not in restricted:
        c += 1
    else:
        m = max(m, c)
        c = 1

print(m)
