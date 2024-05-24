# https://education.yandex.ru/ege/task/4a1efe59-95a4-4665-a2e9-e32dabc2ff12

s = open('4a1efe59-95a4-4665-a2e9-e32dabc2ff12.txt').read()
s = s.replace('B', 'A').replace('2', '1')
c = m = 0
for r in range(0, len(s) - 1, 2):
    a = s[r:r + 2]
    if a == 'A1':
        c += 1
    else:
        m = max(m, c)
        c = 0
print(m)
