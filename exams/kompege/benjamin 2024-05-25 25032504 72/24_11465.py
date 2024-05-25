s = open('24_11465.txt').read()

s = s.replace('C', 'A').replace('B', 'A')
s = s.replace('9', '8')

temp = ''
m = 0
for r in range(1, len(s)):
    a = s[r - 1:r + 1]
    if a != 'AA' and a != '88':
        temp += a[0]
    else:
        m = max(len(temp), m)
        temp = a[0]
print(m)

c = m = 1

for r in range(1, len(s)):
    a = s[r - 1:r + 1]
    if a != 'AA' and a != '88':
        c += 1
    else:
        c = 1
    m = max(m, c)
print(m)
