c = 0
for num in range(700_001, 1_000_000):
    if c == 5:
        break
    delitels = [delitel for delitel in range(2, int(num // 2) + 1) if num % delitel == 0]
    if delitels:
        sum_of = delitels[0] + delitels[-1]
        if (sum_of != num + 1) and (sum_of % 10 == 8):
            print(num, sum_of)
            c += 1
