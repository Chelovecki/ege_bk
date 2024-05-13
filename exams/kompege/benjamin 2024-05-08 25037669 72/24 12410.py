s = open('24_12410.txt').read()

l = 0
c = m = 1
for r in range(1, len(s)):
    if s[r - 1] > s[r]: c += 1
    while c > 100_000:
        if s[l - 1] <= s[l]: c -= 1
        l += 1
    if c == 100_000:
        m = max(m, r - l + 1)
print(m)
