s = open('24_7600.txt').read()

s = s.replace('R', 'Q').replace('S', 'Q')

c = m = 1
for idx in range(len(s) - 1):
    if s[idx - 1] + s[idx] != 'QQ':
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)
