numbers = [list(map(int, r.split(';'))) for r in open('3.csv').readlines()]

c = 0
for line in numbers:
    repeat = [r for r in line if line.count(r) == 2]
    non_repeat = [r for r in line if line.count(r) == 1]
    if len(repeat) == 4 and len(non_repeat) == 3:
        if line.count(max(line)) == 1:
            print(sum(line))
            break
