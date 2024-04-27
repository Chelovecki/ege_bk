numbers = [list(map(int, r.split(';'))) for r in open('46967.csv')]

c = 0
for line in numbers:
    line.sort()
    h = [
        line[0] + line[1] < line[2],
        line[0] + line[1] < line[3]
    ]
    if any(h):
        c += 1
print(c)
