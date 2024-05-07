s = open('24_7624.txt').read()

s = s.replace('Y', 'X').replace('Z', 'X')

c = m = 1

for idx in range(len(s)):
    r = s[idx - 1] + s[idx]
    if r != 'XX':
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)

# при start=0 (как щас) и start=1 результат один и тот же (я про ренж)
