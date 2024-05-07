s = open('24_14642.txt').read()
l = c = m = 0
for r in range(len(s)):
    if s[r] == 'F': c += 1
    while c > 1:
        if s[l] == 'F': c -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)
