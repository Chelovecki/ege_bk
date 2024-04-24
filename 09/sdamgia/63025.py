numbers = [list(map(int, r.split(';'))) for r in open('63025.csv')]

c = 0

for line in numbers:
    c1 = len(line) != len(set(line))
    line.sort()
    c2 = line.count(line[-1]) == 1
    povtor = [r for r in line if line.count(r) >1]
    c3 = sum(povtor) > line[-1]

    if c1 and c2 and c3:
        c += 1
print(c)
