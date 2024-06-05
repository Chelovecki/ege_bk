numbers = [int(r) for r in open('17 2.txt').readlines()]
abs_less_100 = len([r for r in numbers if abs(r) < 100])
c = m = 0
for r in range(1, len(numbers)):
    a = numbers[r - 1:r + 1]
    if (sum(a) / 2) > abs_less_100:
        c += 1
        m = max(sum(a), m)

print(c, m)
