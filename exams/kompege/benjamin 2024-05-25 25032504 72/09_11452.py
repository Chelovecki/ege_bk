numbers = [list(map(int, r.split(';'))) for r in open('9_11452.csv').readlines()]
for n, line in enumerate(numbers, 1):
    a = [r for r in line if line.count(r) == 2]
    if len(a) == 2 and len(set(line)) == 5:
        rep = a[0]
        b = [r for r in line if line.count(r) == 1]
        if rep >= (sum(b) / 4):
            print(n)
            break
