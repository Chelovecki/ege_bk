numbers = [int(r) for r in open('64947.txt')]
max_end_832 = max([r for r in numbers if str(r).endswith('832')])

c = m = 0
for r in range(2, len(numbers)):
    f, s, t = numbers[r - 2:r + 1]
    a = [f, s, t]

    if 0 < len([r for r in a if len(str(abs(r))) == 4]) < 3:
        if len([r for r in a if r % 5 == 0]) > len([r for r in a if r % 3 == 0]):
            if sum(a) > max_end_832:
                c += 1
                m = max(m, sum(a))
print(c, m)
