s = open('24_14647.txt').read()

l = m = x = y = 0
for r in range(len(s)):
    if s[r] == 'X': x += 1
    if s[r] == 'Y': y += 1
    while x > 1 or y > 1:
        if s[l] == 'X': x -= 1
        if s[l] == 'Y': y -= 1
        l += 1

    if x == 1 and y == 1:
        m = max(m, r - l + 1)
print(m)
