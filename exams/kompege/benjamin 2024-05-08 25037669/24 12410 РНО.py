s = open('24_12410.txt').read()
c = m = l = 0
for r in range(1, len(s)):
    if s[r] < s[r - 1]: c += 1

    while c > 100_000:
        if s[l + 1] < s[l]: c -= 1
        l += 1

    if c == 100_000:
        m = max(m, r - l + 1)

print(f"{m:,}")

# как и почему для меня так и осталось загадкой
# todo разобраться как и почему
