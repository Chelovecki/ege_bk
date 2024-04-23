numbers = [list(map(int, r.split(';'))) for r in open('59687.csv')]

c = 0
for line in numbers:
    non_repeat = [r for r in line if line.count(r) == 1]
    repeat = [r for r in line if line.count(r) == 3]
    if repeat:
        povtor_num = [r for r in line if line.count(r) == 3][0]

        sr_rfm = sum(non_repeat) / len(non_repeat)
        c2 = sr_rfm <= povtor_num
        if c2: c += 1
print(c)
