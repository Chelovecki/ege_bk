s = open('24_11954.txt').read()

cy = cx = l = 0
m = 100_000

for r in range(len(s)):
    if s[r] == 'X': cx += 1
    if s[r] == 'Y': cy += 1

    while cx >= 500:
        if cy == 0: m = min(m, r - l + 1)
        if s[l] == 'X': cx -= 1
        if s[l] == 'Y': cy -= 1
        l += 1
print(m)
