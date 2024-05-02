numbers = [list(map(int, r.split(';'))) for r in open('59833.csv')]
c = 0

for line in numbers:
    repeat = [r for r in line if line.count(r) == 2]

    if len(repeat) == 2:
        sr = [r for r in line if r not in repeat]
        if sum(sr) / len(sr) > repeat[0]:
            c += 1
print(c)
