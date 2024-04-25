numbers = [list(map(int, r.split(';'))) for r in open('64894.csv')]
nums_by_col = [[line[id_col] for line in numbers] for id_col in range(len(numbers[0]))]

c = 0
for line in numbers:
    c_good_line = 0
    for id in range(len(line)):
        this_num = line[id]
        if line.count(this_num) == 1 and nums_by_col[id].count(this_num) > 150:
            c_good_line += 1
    if c_good_line >= 5:
        c += 1
print(c)
