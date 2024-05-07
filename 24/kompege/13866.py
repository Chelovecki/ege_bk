s = open('24_13866.txt').read()
for r in '3579':
    s = s.replace(r, '1')
c = m = 2

for idx in range(2, len(s)):
    b = s[idx - 2:idx + 1]
    if b == '111':
        m = max(m, c)
        c = 2
    else:
        c += 1
print(m)
