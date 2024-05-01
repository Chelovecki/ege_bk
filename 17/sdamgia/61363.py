numbers = [int(r) for r in open('61363.txt').readlines()]
max_ends_19 = max([r for r in numbers if str(r).endswith('19')])

c = m = 0
for id in range(2, len(numbers)):
    f, s, t = numbers[id - 2:id + 1]

    if len([r for r in [f, s, t] if len(str(abs(r))) == 4]) == 2:
        if len([r for r in [f, s, t] if r % 3 == 0]) >= 1:
            if (f + s + t) > max_ends_19:
                c += 1
                m = max(m, f + s + t)
print(c, m)
