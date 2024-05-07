s = open('24_7272.txt').read()
s = s.replace('AB', '**').replace('CB', '**')

c = m = 0
for r in s:
    if r == '*':
        c += 1
    else:
        m = max(c, m)
        c = 0
print(m // 2)
# //2 так как мы считали символы, а надо считать ПАРЫ, так что делим на 2
