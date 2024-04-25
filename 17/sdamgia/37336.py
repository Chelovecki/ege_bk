numbers = [int(r) for r in open('37336.txt').readlines()]

c = m = 0
for idx in range(1, len(numbers)):
    f = numbers[idx - 1]
    s = numbers[idx]

    c1 = any([f % 3 == 0, s % 3 == 0])

    if c1:
        c += 1
        m = max(m, f + s)
print(c, m)
