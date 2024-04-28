s = open('38958.txt').read()

l = m = 0
ca = 0
for r in range(1, len(s)):
    if s[r] == 'A': ca += 1
    while ca > 1:
        if s[l] == 'A': ca -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)
