numbers = [int(r) for r in open('17.txt').readlines()]
max_ends_121 = max([r for r in numbers if str(r).endswith('121')])
c = m = 0

for r in range(2, len(numbers)):
    a = numbers[r - 2:r + 1]
    if len([num for num in a if len(str(abs(num))) == 4 and num % 2 == 0]) <= 1:
        if sum(a) <= max_ends_121:
            c += 1
            m = max(m, sum(a))
print(c, m)
