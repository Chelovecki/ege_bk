numbers = [int(r) for r in open('17.txt').readlines()]
max_krat_401 = max([r for r in numbers if r % 401 == 0])
c = 0
m = max(numbers)
for r in range(2, len(numbers)):
    n = numbers[r - 2:r + 1]
    b = [sum(map(int, list(str(obj)))) for obj in n]
    if len(b) == len(set(b)):
        if sum(n) > max_krat_401:
            c += 1
            m = min(m, sum(n))
print(c, m)
