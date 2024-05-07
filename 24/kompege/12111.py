s = open('24_12111.txt').read()
c = m = 0
for idx_start in range(3):
    for idx in range(idx_start, len(s) - 2, 3):
        b = s[idx:idx + 3]
        if b == 'HPY' or b == 'NYN':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
