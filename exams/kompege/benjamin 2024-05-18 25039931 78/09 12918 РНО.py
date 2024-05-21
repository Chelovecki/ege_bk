numbers = [list(map(int, r.split(';'))) for r in open('9_12918.csv').readlines()]

for line in numbers:
    if len(set([r for r in line if line.count(r) == 2])) == 2 and len([r for r in line if line.count(r) == 1]) == 2:
        if line.count(max(line)) == 1:
            line.sort()
            if (line[0] * line[-1]) > sum(line[1:6]):
                print(sum(line))
                break
