s = open('24_11892.txt').read()

c_x = c_y = l = 0
m = len(s)

for r in range(len(s)):
    if s[r] == 'X': c_x += 1
    if s[r] == 'Y': c_y += 1
    while c_y > 0 or c_x > 500:
        if s[l] == 'Y': c_y -= 1
        if s[l] == 'X': c_x -= 1
        l += 1
    if c_x >= 500 and c_y == 0:
        m = min(m, r - l + 1)
print(m)
