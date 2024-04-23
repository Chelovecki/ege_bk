n_by_row = [list(map(int, r.split(';'))) for r in open('64939.csv')]
c = 0
n_by_col = [[n_by_row[num_in_row][col_id] for num_in_row in range(len(n_by_row))] for col_id in range(6)]
for row in range(len(n_by_row)):
    good_int_row = 0
    for col in range(6):
        num = n_by_row[row][col]
        if n_by_row[row].count(num) == 1 and n_by_col[col].count(num) < 170:
            good_int_row += 1
    if good_int_row >= 4:
        c += 1
print(c)
