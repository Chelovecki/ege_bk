s = open('24_9882.txt').read()

c = 0

m = len(s)
l = 0
for r in range(len(s)):
    if s[r] in 'BC': c += 1
    while c > 127:
        if s[l] in 'BC': c -= 1
        l += 1
    if c == 127:
        m = min(m, r - l + 1)
print(m)
