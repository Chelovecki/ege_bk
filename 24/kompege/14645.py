import string

s = open('24_14645.txt').read()

glas = 'AEIOUY'
not_glas = 'BCDFGHJKLMNPQRSTVWXZ'

flag = False
m = 0
c = 1

for idx in range(1, len(s)):
    if flag:
        m = max(m, c)
    if (s[idx] in glas and s[idx - 1] in not_glas) or (s[idx] in not_glas and s[idx - 1] in glas):
        flag = True
        c += 1
    else:
        flag = False
        c = 1

print(m)
