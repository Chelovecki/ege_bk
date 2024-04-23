numbers = [list(map(int, r.split(';'))) for r in open('48430.csv')]

c = 0
for line in numbers:
    frequency = [line.count(r) for r in line]
    repeating = set([r for r in line if line.count(r) == 2])
    non_repeating = [r for r in line if line.count(r) == 1]

    c1 = frequency.count(2) == 4 and frequency.count(1) == 2
    if c1:
        c2 = sum(repeating) < sum(non_repeating)
        if c2: c += 1
print(c)
