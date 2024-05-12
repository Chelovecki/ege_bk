numbers = [list(map(int, r.split(';'))) for r in open('9.csv').readlines()]

c = 0
for line in numbers:
    if len(line) == len(set(line)):
        line.sort()
        a = (line[0] + line[-1]) * 2
        b = sum((line[1], line[2], line[3]))
        if a <= b:
            c += 1
print(c)
