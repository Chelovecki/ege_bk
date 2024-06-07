m = 0
for n in range(4, 10_001):
    s = '1' + '9' * n
    while '19' in s or '49' in s or '999' in s:
        if '19' in s: s = s.replace('19', '9', 1)
        if '49' in s: s = s.replace('49', '91', 1)
        if '999' in s: s = s.replace('999', '4', 1)
    a = sum([int(r) for r in s])
    m = max(a, m)
print(m)
