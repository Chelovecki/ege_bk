numbers = [list(map(int, r.split(';'))) for r in open('09 68510.csv').readlines()]

c = 0
for line in numbers:
    line.sort()
    if line[-1] < sum(line[:3]):
        a, b, c, d = line
        if a + b == c + d or a + c == b + d or a + d == b + c:
            c += 1
print(c)
