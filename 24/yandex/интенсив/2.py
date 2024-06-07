s = open('2.txt').read()

c = m = 1
for r in range(1, len(s)):
    if s[r - 1] != s[r]:
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)
