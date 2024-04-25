numbers = [list(map(int, r.split(';'))) for r in open('46967.csv')]

c = 0
for line in numbers:
    line.sort()
    if line[0] + line[1] < line[2] or line[0] + line[1] < line[3]:
        c += 1
print(c)
