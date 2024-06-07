numbers = [int(r) for r in open('17 6.txt').readlines()]
max_abs_krat_570 = max(abs(r) for r in numbers if abs(r) % 570 == 0)
c4 = 0
for r in range(3, len(numbers)):
    a = numbers[r - 3:r + 1]
    if (sum(a) / len(a)) > max_abs_krat_570:
        c4 += 1

c3 = 0
for r in range(2, len(numbers)):
    a = numbers[r - 2:r + 1]
    if len([n for n in a if n > 0]) >= 2:
        if sum(a) % 34 == 0:
            c3 += 1
print(c4, c3)
