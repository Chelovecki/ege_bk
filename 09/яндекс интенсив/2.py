numbers = [list(map(int, r.split(';'))) for r in open('2.csv').readlines()]

for n, line in enumerate(numbers, 1):
    repeat = [r for r in line if line.count(r) == 2]
    non_repeat = [r for r in line if line.count(r) == 1]
    if len(repeat) == 2 and len(non_repeat) == 4:
        if repeat[0] >= (sum(non_repeat) / len(non_repeat)):
            print(n)
            break
