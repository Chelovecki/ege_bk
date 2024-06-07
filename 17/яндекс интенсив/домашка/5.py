numbers = [int(r) for r in open('17 5.txt').readlines()]
max_ends_0F = max(r for r in numbers if hex(r).endswith('0f'))
c = m = 0
for r in range(1, len(numbers)):
    a = numbers[r - 1:r + 1]
    if len([b for b in a if b % 7 == 0]) == 1:
        if sum(a) % max_ends_0F == 0:
            c += 1
            m = max(sum(a), m)

print(c, m)
