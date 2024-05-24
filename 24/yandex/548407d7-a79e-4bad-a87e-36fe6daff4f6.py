# https://education.yandex.ru/ege/task/548407d7-a79e-4bad-a87e-36fe6daff4f6

s = open('548407d7-a79e-4bad-a87e-36fe6daff4f6.txt').read()

l = m = c = t = 0
for r in range(len(s)):
    if s[r] == 'T':
        t += 1
    while t > 100:
        if s[l] == 'T': t -= 1
        l += 1
    if t == 100:
        m = max(m, r - l + 1)
print(m)
