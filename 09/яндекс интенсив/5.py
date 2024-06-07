numbers = [list(map(int, r.split(';'))) for r in open('5.csv').readlines()]

for n, line in enumerate(numbers, 1):
    repeat = [r for r in line if line.count(r) == 3]
    non_repeat = [r for r in line if line.count(r) == 1]
    if len(repeat) == 3 and len(non_repeat) == 4:
        chet = [r for r in line if r % 2 == 0]
        nechet = [r for r in line if r % 2 != 0]
        if len(chet) > len(nechet):
            print(n)
