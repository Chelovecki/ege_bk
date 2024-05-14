numbers = [list(map(int, r.split(';'))) for r in open('9.csv').readlines()]

numbers_by_col = [[numbers[col][row] for col in range(len(numbers))] for row in range(len(numbers[0]))]

for n, line in enumerate(numbers,1):
    c_tri = 0
    for idx_start in range(len(line) - 1):
        for idx_compare in range(idx_start, len(line)):
            if line[idx_compare] % 2 == 0:
                c_tri += 1
                break
    if c_tri >= 3:
        if any([numbers_by_col[idx_].count(line[idx_]) == line.count(line[idx_]) for idx_ in range(len(line))]):
            print(n)

