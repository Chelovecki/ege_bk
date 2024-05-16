numbers = [int(r) for r in open('17 68518.txt').readlines()]
min_krat_19 = min([r for r in numbers if r % 19 == 0])
c = m = 0

for r in range(1, len(numbers)):
    this_2_nums = numbers[r - 1:r + 1]
    first, second = this_2_nums
    if first % min_krat_19 == 0 or second % min_krat_19 == 0:
        c += 1
        m = max(m, first + second)
print(c, m)
