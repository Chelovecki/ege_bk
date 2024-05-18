s = open('24 68525.txt').read()

c = m = 1
s = s.replace('R', 'Q').replace('W', 'Q').replace('2', '1').replace('4', '1')
for r in range(1, len(s)):
    a = s[r - 1] + s[r]
    if a != '11' and a != 'QQ':
        c += 1
    else:
        m = max(c, m)
        c = 1
print(m)
