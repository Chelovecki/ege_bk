s = open('58326.txt').read()

# 1 так как у нас как минимум будет 1 подходящая подстрока длиной 1
c = m = 1
for r in range(1, len(s)):
    first = s[r - 1]
    second = s[r]
    if first < second:
        c += 1
    else:
        m = max(c, m)
        c = 1

print(m)
