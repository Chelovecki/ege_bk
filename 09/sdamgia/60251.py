numbers = [list(map(int, r.split(';'))) for r in open('60251.csv')]

c = 0
for line in numbers:
    frequency = [line.count(r) for r in line]
    repeat = [r for r in line if line.count(r) == 2]
    non_repeat = [r for r in line if line.count(r) == 1]

    c1 = frequency.count(1) == 3
    if c1:
        povt = sum(repeat) / len(repeat)
        not_povt = sum(non_repeat) / len(non_repeat)
        if povt < not_povt: c += 1
print(c)
