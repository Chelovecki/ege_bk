numbers = [int(r) for r in open('17_12450.txt').readlines()]
min_krat_52 = min([r for r in numbers if r % 52 == 0])
c = m = 0

for idx in range(2, len(numbers)):
    seq = numbers[idx - 2:idx + 1]
    if sum([r % 113 for r in seq]) == min_krat_52:
        c += 1
        m = max(m, sum(seq))
print(c, m)
