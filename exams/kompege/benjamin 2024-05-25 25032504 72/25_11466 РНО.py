def div(x):
    for delitel in range(10, x):
        if x % delitel == 0 and str(delitel).endswith('9'):
            return delitel


c = 0
for r in range(600_001, 10_000_000):
    a = div(r)
    if c == 5:
        break
    if a:
        print(r, a)
        c += 1
