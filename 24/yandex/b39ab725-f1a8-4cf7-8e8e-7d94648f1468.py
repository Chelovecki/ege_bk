# https://education.yandex.ru/ege/task/b39ab725-f1a8-4cf7-8e8e-7d94648f1468

s = open('b39ab725-f1a8-4cf7-8e8e-7d94648f1468.txt').read()

x = y = l = m = 0
c = 0
temp = s[0]
for r in range(1, len(s)):
    a = s[r - 1:r + 1]
    if a == 'XX' or a == "YY":
        m = max(m, len(temp))
        temp = s[r]
    else:
        temp += s[r]
print(m)
