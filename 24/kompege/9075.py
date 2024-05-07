s = open('24_9075.txt').read()
for r in '2468':
    s = s.replace(r, '0')

for r in '3579':
    s = s.replace(r, '1')
m = c = 1
for r in range(1, len(s)):
    a = s[r - 1] + s[r]
    if a != '01' and a != '10':
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)
