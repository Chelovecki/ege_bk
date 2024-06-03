for r in range(4,10_001):
    s = "3" + "9"*r
    while '9999' in s or '933' in s or '3339' in s:
        if '9999' in s: s=s.replace('9999','3',1)
        if '933' in s: s=s.replace('933','55',1)
        if '3339' in s: s=s.replace('3339','93',1)

    s = sum([int(symb) for symb in s])
    if s==70:
        print(r)