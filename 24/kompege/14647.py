s = open('24_14647.txt').read()

l = c_x = c_y = m = 0

for r in range(len(s)):
    if s[r] == 'X': c_x += 1
    if s[r] == 'Y': c_y += 1
    while c_y > 1 or c_x > 1:
        if s[l] == 'X': c_x -= 1
        if s[l] == 'Y': c_y -= 1
        l += 1
    if c_x == 1 and c_y == 1:
        m = max(m, r - l + 1)
print(m)
