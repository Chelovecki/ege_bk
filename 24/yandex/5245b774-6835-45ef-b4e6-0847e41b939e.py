# https://education.yandex.ru/ege/task/5245b774-6835-45ef-b4e6-0847e41b939e

s = open('5245b774-6835-45ef-b4e6-0847e41b939e.txt').read()

m = c = 0

for r in range(1, len(s), 2):
    a = s[r:r + 2]
    if a == 'AA' or a == 'CC':
        c += 1
    else:
        m = max(m, c)
        c = 0
print(m)
