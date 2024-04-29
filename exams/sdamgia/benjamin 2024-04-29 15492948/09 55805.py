numbers = [list(map(int, r.split(';'))) for r in open('09 55805.csv')]

c = 0
for line in numbers:
    if len([r for r in line if line.count(r) == 1]) == len(line):
        line.sort()
        if (line[-1] + line[0]) * 3 <= (line[1] + line[2] + line[3]) * 2:
            c += 1
print(c)
