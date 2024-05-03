s = open('24_5381.txt').read()

s = s.replace('E', 'A').replace('U', 'A')
s = s.replace('C', 'B').replace('D', 'B').replace('F', 'B')

c = 0
m = 0
l = 2
for r in range(2, len(s)):
    a = s[r - 2:r + 1]
    if a == 'BAB':
        c += 1
    while c > 2:
        b = s[l - 2:l + 1]
        if b == 'BAB': c -= 1
        l += 1
    if c == 2: m = max(m, r - l + 1)
print(m + 2)
