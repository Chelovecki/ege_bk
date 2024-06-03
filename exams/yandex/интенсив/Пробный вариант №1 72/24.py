s = open('24.txt').read()
l = c = m = 0

for r in range(len(s)):
    if s[r] == 'A': c += 1
    while c > 240:
        if s[l] == 'A': c -= 1
        l += 1
    if c == 240:
        m = max(m, r - l + 1)
print(m)
