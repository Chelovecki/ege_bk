numbers = [int(r) for r in open('17_11460.txt').readlines()]
max_starts_8 = max([r for r in numbers if str(abs(r))[0] == '8'])
c = 0
m = 100_000

for idx in range(2, len(numbers)):
    a = numbers[idx - 2:idx + 1]
    if len([r for r in a if str(abs(r))[0] == '6']) <= 1:
        if sum(a) >= max_starts_8:
            c += 1
            m = min(m, sum(a))
print(c, m)
