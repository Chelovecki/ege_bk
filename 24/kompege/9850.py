s_copy = open('24_9850.txt').read()

restricted = 'LISENOK'
s = s_copy
c = m = 0
for r in range(len(s)):
    if s[r] not in restricted:
        c += 1
        m = max(c, m)
    else:
        c = 0
print(m)

print('------------')
s = s_copy

for r in restricted:
    s = s.replace(r, ' ')

print(max(len(r) for r in s.split()))
