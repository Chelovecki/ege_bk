numbers = [list(map(int, r.split(';'))) for r in open('59780.csv')]

c = 0
for line in numbers:
    repeat = [r for r in line if line.count(r) == 4]
    if repeat:
        num = repeat[0]
        if num < (sum(line) / len(line)): c += 1
print(c)
