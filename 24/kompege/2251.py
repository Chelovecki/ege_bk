s = open('24_2251.txt').read()

l = m = c = 0

for r in range(len(s)):
    if s[r] == 'D': c += 1
    while c > 2:
        # главное не обосраться, и не поставить s[r]
        if s[l] == 'D': c -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)
