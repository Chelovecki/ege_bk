s = open('24 59729.txt').read()
c = l = 0
m = len(s)
s = s.replace('TT', '*')

for r in range(len(s)):
    if s[r] == '*': c += 1
    while c > 150:
        if s[l] == '*': c -= 1
        l += 1
    if c == 150: m = min(m, r - l + 1)
print(m)
