numbers = [int(r) for r in open('17 4.txt').readlines()]
max_ends_18 = max(r for r in numbers if str(r).endswith('18'))
c = m = 0
for r in range(2, len(numbers)):
    a = numbers[r - 2:r + 1]
    if len([b for b in a if str(b).count('3') > 0]) <= 2:
        if sum(a) <= max_ends_18:
            c += 1
            m = max(sum(a), m)

print(c, m)
