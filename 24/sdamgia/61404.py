"""
Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное количество идущих подряд символов, среди которых ровно по одному разу встречаются буквы X и Y.
"""

s = open('61404.txt').read()

l = m = cx = cy = 0

for r in range(len(s)):
    b = s[l:r + 1]

    if s[r] == 'X': cx += 1
    if s[r] == 'Y': cy += 1

    while cx > 1 or cy > 1:
        if s[l] == 'X': cx -= 1
        if s[l] == 'Y': cy -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)