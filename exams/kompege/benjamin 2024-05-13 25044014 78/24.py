s = open('24.txt').read()

c = m = 0
for r in range(3, len(s)):
    a = s[r - 3:r + 1]
    if a != 'XZZY':
        c += len(a)
    else:
        m = max(m, c)
        c = 0
print(m)

# --------------------------

c = m = 0
temp = ''
for r in range(3, len(s)):
    a = s[r - 3:r + 1]
    temp += a
    if 'XZZY' not in temp:
        m = max(m, len(temp))
    else:
        temp = ''
print(m)
