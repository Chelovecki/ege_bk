numbers = [list(map(int, r.split(';'))) for r in open('55596.csv')]

flat_list = [r for line in numbers for r in line]
frequency = dict.fromkeys(set(flat_list), 0)
for num in flat_list:
    frequency[num] += 1

c = 0

for line in numbers:
    for num in line:
        if frequency[num] == 46 and line.count(num) == 1:
            c += 1
            break
print(c)

