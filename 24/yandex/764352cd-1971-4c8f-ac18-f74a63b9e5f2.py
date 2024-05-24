# https://education.yandex.ru/ege/task/764352cd-1971-4c8f-ac18-f74a63b9e5f2

s = open('764352cd-1971-4c8f-ac18-f74a63b9e5f2.txt').read()

s = s.replace('O', 'A').replace('D', 'C').replace('F', 'C')

l = m = c = 0

for r in range(0, len(s), 2):
    a = s[r:r + 2]
    if a == 'CA': c += 1
    while c > 5:
        b = s[l:l + 2]
        if b == 'CA': c -= 1
        l += 1
    if c == 5:
        m - max(m, r - l + 1)
print(m)
