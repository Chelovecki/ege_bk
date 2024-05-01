numbers = [int(r) for r in open('17 59695.txt')]
max_ends_15 = max([r for r in numbers if str(r).endswith('15')])
c = m = 0
for id in range(2, len(numbers)):
    f, s, t = numbers[id - 2:id + 1]
    a = numbers[id - 2:id + 1]

    if len([r for r in a if len(str(r)) == 4]) == 1:
        if sum(a) >= max_ends_15:
            c += 1
            m = max(m, sum(a))
print(c, m)
