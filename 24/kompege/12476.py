s = open('24_12476.txt').read()

l = m = c = 0

for r in range(len(s) - 1):
    if s[r - 1:r + 1] == 'RO': c += 1
    while c > 21:
        if s[l:l + 2] == 'RO': c -= 1
        l += 1
    if 'ORO' not in s[l:r + 1] and 'ROR' not in s[l:r + 1]:
        m = max(m, r - l + 1)
print(m)
