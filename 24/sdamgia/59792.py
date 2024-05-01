s = open('59792.txt').read()

l = c = 0
m = 10**6
for r in range(1, len(s)):
    if s[r] == 'T':
        c += 1
    while c > 100:
        if s[l] == 'T':
            c -= 1
            l += 1
    m = min(m, r - l + 1)
print(m)
#todo