data = [list(map(int, r.split(';'))) for r in open('61355.csv')]

c = 0
for line in data:
    # все различны
    c1 = len(line) == len(set(line))

    line.sort()
    c2 = ((line[0] + line[-1]) / 2) > (sum(line[1:5]) / 4)
    if c1 and c2: c += 1
print(c)
