s = open('24_8959.txt').read()

s = s.replace('EA', '**').replace('NPC', '***')

c = m = 0
for r in s:
    if r == '*':
        c += 1
    else:
        m = max(m, c)
        c = 0
print(m)
