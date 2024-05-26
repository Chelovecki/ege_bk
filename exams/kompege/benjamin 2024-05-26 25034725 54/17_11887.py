numbers = [int(r) for r in open('17_11887.txt').readlines()]
max_end_68 = max([r for r in numbers if str(r).endswith('68')])
c = m = 0

for r in range(3, len(numbers)):
    a = numbers[r - 3:r + 1]
    log1 = len([r for r in a if 10 <= abs(r) <= 99])
    if log1 == 1 or log1 == 4:
        if sum(a) >= max_end_68:
            c += 1
            m = max(m, sum(a))
print(c, m)
