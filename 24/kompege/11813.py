s_copy = open('24_11813.txt').read()
# ----------------------------
s = s_copy
glas = 'AEIOUY'
neglas = 'BCDFGHJKLMNPQRSTVWXZ'

c = m = 1
for idx in range(1, len(s_copy)):
    if (s_copy[idx - 1] in glas and s_copy[idx] in neglas) or (s_copy[idx - 1] in neglas and s_copy[idx] in glas):
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)

print("----------------------------------------------")

s = s_copy
for r in glas[1:]:
    s = s.replace(r, 'A')

for r in neglas[1:]:
    s = s.replace(r, 'B')
c = m = 1
for idx in range(1, len(s)):
    if s[idx - 1] != s[idx]:
        c += 1
        m = max(c, m)
    else:
        c = 1
print(m)


print("----------------------------------------------")

# код ниже почему-то выдает 23
# s = s_copy
# for r in glas[1:]:
#     s = s.replace(r, 'A')
#
# for r in neglas[1:]:
#     s = s.replace(r, 'B')
# s = s.replace('AA', ' ').replace('BB',' ')
# print(max(len(r) for r in s.split()))
