s = open('24_2251.txt').read()

m = l = c = 0
for r in range(len(s)):
    if s[r] == 'D': c += 1

    while c > 2:
        if s[r] == 'D': c -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)
