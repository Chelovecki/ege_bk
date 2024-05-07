s = open('24_9845.txt').read()

s = s.replace('B', 'A').replace('C', 'A').replace('9', '8')

c = m = 1

for idx in range(1, len(s)):
    a = s[idx - 1:idx + 1]
    if a != 'AA' and a != '88':
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)
