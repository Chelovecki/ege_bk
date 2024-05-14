s = open('24.txt').read()

d = [3] * len(s)

for r in range(3, len(s)):
    if s[r - 3:r + 1] != 'XZZY':
        d[r] = d[r - 1] + 1
print(max(d))

s = s.replace('XZZY', ' ')

print(max([len(r) for r in s.split()]) + len('ZZY') + len('XZZ'))
