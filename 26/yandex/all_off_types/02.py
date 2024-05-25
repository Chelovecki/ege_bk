f = open('02 orig data.txt')

n = int(f.readline())
data = sorted([list(map(int, line.split())) for line in f.readlines()])

rows = dict.fromkeys([r[0] for r in data], None)

for line in data:
    a,b = line

    if rows[a] is None:
        rows[a] = []
    rows[a].append(b)

unique_rows = sorted(set([r[0] for r in data]))

for id_row in unique_rows:
    line = rows[id_row]
    line.sort()
    for idx in range(1,len(line)):
        if line[idx] - line[idx-1]-1 == 13:
            print(id_row,line[idx-1]+1)
            break

