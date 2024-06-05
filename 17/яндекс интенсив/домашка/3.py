numbers = [int(r) for r in open('17 3.txt').readlines()]
min_krat_103 = min(r for r in numbers if r % 103 == 0)
c = m = 0
for r in range(1, len(numbers)):
    a = numbers[r - 1:r + 1]
    if sum(a) % 2 == 0 and ((a[0] - a[1]) % min_krat_103 == 0):
        c += 1
        m = max(sum(a), m)

print(c, m)
