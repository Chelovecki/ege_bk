numbers = [int(r) for r in open('59784.txt')]

max_end_15 = max([r for r in numbers if str(r).endswith('15')])

c = 0
m = float('inf')
for r in range(2, len(numbers)):
    f, s, t = numbers[r - 2:r + 1]
    a = [f, s, t]

    if len([r for r in a if len(str(abs(r))) == 4]) == 1:
        if sum(a) < max_end_15:
            c += 1
            m = min(m, sum(a))
print(c, m)
