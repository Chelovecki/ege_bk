numbers = [int(r) for r in open('37341.txt')]
c = m = 0
for idx_f in range(len(numbers) - 1):
    for idx_s in range(idx_f + 1, len(numbers)):
        f = numbers[idx_f]
        s = numbers[idx_s]

        c1 = (f - s) % 2 == 0

        if c1 and (f % 19 == 0 or s % 19 == 0):
            c += 1
            m = max(m, f + s)
print(c, m)
