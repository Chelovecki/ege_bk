numbers = [list(map(int, r.split(';'))) for r in open('1.csv').readlines()]

c = 0
for line in numbers:
    non_repeat = [r for r in line if line.count(r) == 1]
    if len(non_repeat) == 1:
        repeat = [r for r in line if line.count(r) == 2]
        if len(repeat) ==6:
            repeat.sort()
            if (repeat[-1] + repeat[0]) / 2 < non_repeat[0]:
                c+=1
print(c)
