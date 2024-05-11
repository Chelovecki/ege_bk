numbers = [list(map(int, r.split(';'))) for r in open('9.csv').readlines()]

c = 0
for n, line in enumerate(numbers, 1):
    c1 = all([line[r - 1] % 2 != line[r] % 2 for r in range(1, 7)])
    if len(line) == len(set(line)):
        proizv_rep = 0
    else:
        proizv_rep = 1
        for r in [b for b in line if line.count(b) > 1]:
            proizv_rep *= r
    c2 = 3 * sum([b for b in line if line.count(b) == 1]) >= proizv_rep

    if c1 and c2:
        c += 1
print(c)
