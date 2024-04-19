s = open('24_10105.txt').read()

l = m = c = 0

for r in range(len(s)):
    if s[r] == 'T': c += 1

    while c > 100:
        if s[l] == 'T': c -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)
