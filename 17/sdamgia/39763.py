numbers = [int(r) for r in open('39763.txt')]
c = m = 0
for idx in range(2, len(numbers)):
    a = sorted(numbers[idx - 2:idx + 1])

    if a[-1] ** 2 < a[0] ** 2 + a[1] ** 2:
        c += 1
        m = max(m, sum(a))

print(c, m)
