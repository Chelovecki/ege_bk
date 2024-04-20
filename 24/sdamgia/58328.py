s = open("24_58328.txt").read()
c = m = 1

for idx in range(1, len(s)):
    first = s[idx - 1]
    second = s[idx]
    if first != second:
        c += 1
    else:
        c =1
    m = max(c, m)

print(m)
