for r in range(4,10_000):
    s = '5'+'2'*r
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:s=s.replace('52','11',1)
        if '2222' in s:s=s.replace('2222','5',1)
        if '1122' in s:s=s.replace('1122','25',1)
    res = sum([int(b) for b in s])
    if res==64:
        print(r)