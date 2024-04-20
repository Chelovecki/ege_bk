file = open('52180.csv')
data = [list(map(int, r.split(';'))) for r in file.readlines()]

c = 0
for line in data:
    chet = [r for r in line if r % 2 == 0]
    nechet = [r for r in line if r % 2 == 1]

    c1 = len(line) == len(set(line))
    c2 = len(chet) > len(nechet)
    c3 = sum(chet) < sum(nechet)

    if c2 and c1 and c3:
        c += 1
print(c)
