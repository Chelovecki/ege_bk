numbers = [list(map(int,r.split(';'))) for r in open('9_12490.csv').readlines()]
c=0
for line in numbers:
    if len([r for r in line if line.count(r)==2]) and len(set(line))+1 == len(line):
        line.sort()
        if line.count(line[-1])== line.count(line[0]):
            c+=1
print(c)
