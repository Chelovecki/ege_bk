numbers = [int(r) for r in open('17.txt').readlines()]
max_ends_42 = max([r for r in numbers if abs(r) % 100 == 42]) ** 2
c = m = 0

for id in range(2, len(numbers)):
    line = numbers[id - 2:id + 1]
    if len([r for r in line if abs(r) % 100 == 42]) >= 2:
        proizv = 1
        for elem in line: proizv *= elem
        if proizv > max_ends_42:
            c += 1
            m = max(m, proizv)
print(c, m)
