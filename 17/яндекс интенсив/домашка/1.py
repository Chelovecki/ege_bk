numbers = [int(r) for r in open('17 1.txt').readlines()]
min_krat_21 = min(r for r in numbers if r % 21 == 0)
c = m = 0
for r in range(1, len(numbers)):
    a = numbers[r - 1:r + 1]
    if any(num % min_krat_21 == 0 for num in a):
        c += 1
        m = max(sum(a), m)

print(c, m)
