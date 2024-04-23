numbers = [list(map(int, r.split(';'))) for r in open('59778.csv')]

c = 0
for line in numbers:
    frequency = [line.count(r) for r in line]
    rep = [r for r in line if line.count(r) == 3]

    not_rep = [r for r in line if line.count(r) == 1]

    if len(rep) == 3 and len(not_rep) == 4:

        if (sum(not_rep) / 4) <= rep[0]:
            c += 1
print(c)


