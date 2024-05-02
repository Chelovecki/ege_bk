import itertools

numbers = [list(map(int, r.split(';'))) for r in open('47006.csv')]

c = 0

for line in numbers:
    if all(r[0] + r[1] > r[2] for r in itertools.permutations(line, 3)):
        c += 1
print(c)
