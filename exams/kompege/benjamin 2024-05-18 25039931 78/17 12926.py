numbers = [int(r) for r in open('17_12926.txt').readlines()]

max_sum_4 = -10_000
for r in range(3, len(numbers)):
    line = numbers[r - 3:r + 1]
    if len(set([str(n)[-1] for n in line])) == 1:
        max_sum_4 = max(max_sum_4, sum(line))


max_dvuzn_ends_10 = max([r for r in numbers if len(str(abs(r))) == 2])


c = 0
m = 10_000


for idx in range(4, len(numbers)):
    line = numbers[idx - 4:idx + 1]

    if len([r for r in line if r < max_sum_4]) == 1:
        if sum(line) % max_dvuzn_ends_10 == 0:
            c += 1
            m = min(m, sum(line))
print(c, m)

