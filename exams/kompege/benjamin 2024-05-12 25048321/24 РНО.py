s = open('24.txt').read()

c = m = 0
for r in range(1, len(s) - 3, 3):
    a = s[r] + s[r + 1] + s[r + 2]
    if a == 'NPO' or a == 'PNO':
        c += 1
    else:
        m = max(m, c)
        c = 0

print(m)
