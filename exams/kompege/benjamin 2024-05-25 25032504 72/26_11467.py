f =open('26_11467.txt')
total_len = int(f.readline())

data = sorted([list(map(int,r.split())) for r in f.readlines()])

c = 0

b = list(set([r[0] for r in data]))
ay_52 = dict.fromkeys(b,0)


time_start = sorted([r[0] for r in data])
time_end = []
for obj in set(time_start):
    for r in data:
        if r[0] == obj:
            time_end.append(r[1])
            break
for r in zip(time_start, time_end):
    print(r)
    break
