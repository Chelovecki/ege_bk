import itertools

s = open('24_8567.txt').read()

restricted = ["".join(r) for r in itertools.product('ABCD', repeat=3)]

c = m = 2
for r in range(len(s) - 2):
    cur = s[r:r + 3]
    if all([cur not in cur_res for cur_res in restricted]):
        c += 1
    else:
        m = max(m, c)
        c = 2
print(m)
