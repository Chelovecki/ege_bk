numbers = [list(map(int, r.split(';'))) for r in open('56537.csv')]

c = 0
for line in numbers:
    frequency = [line.count(r) for r in line]

    c1 = frequency.count(1) > 0

    repeat = [r for r in line if line.count(r) != 1]
    non_repeat = [r for r in line if line.count(r) == 1]
    if repeat and non_repeat:
        c2 = (sum(non_repeat) / len(non_repeat)) < (sum(repeat) / len(repeat))
        if c1 and c2: c += 1

print(c)
