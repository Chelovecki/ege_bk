numbers = [list(map(int, r.split(';'))) for r in open('9_ok_11879.csv').readlines()]

c = 0

for line in numbers:
    log1 = len([r for r in line if line.count(r) == 3]) == 3 and len([r for r in line if line.count(r) == 1]) == 4
    log2 = line == sorted(line)
    if log1 + log2 < 2:
        c += 1
print(c)
