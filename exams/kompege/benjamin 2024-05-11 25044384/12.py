m=0
for n in range(4, 10_000):
    s = '8' + '7' * n
    while '57' in s or '877' in s or '777' in s:
        if '57' in s: s = s.replace('57', '7', 1)
        if '877' in s: s = s.replace('877', '75', 1)
        if '777' in s: s = s.replace('777', '8', 1)
    b=1
    for r in map(int,list(s)):
       b*=r
    m=max(m,b)
print(m)