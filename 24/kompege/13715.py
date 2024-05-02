s = open('24_13715.txt').read()

l = m = c = 0

for r in range(1, len(s)):
    a = s[r - 1] + s[r]
    if a == 'AB': c += 1

    while c > 50:
        if s[l] + s[l + 1] == 'AB': c -= 1
        l += 1
    if c == 50:
        m = max(m, r - l + 1)

print(m)
