s = open('63040.txt').read()

c_a = c_b = l = m = 0
for r in range(len(s)):
    if s[r] == 'A': c_a += 1
    if s[r] == 'B': c_b += 1
    while c_a > 2 or c_b > 2:
        if s[l] == 'A': c_a -= 1
        if s[l] == 'B': c_b -= 1
        l += 1
    if c_a <= 2 or c_b <= 2:
        m = max(m, r - l + 1)
print(m)
