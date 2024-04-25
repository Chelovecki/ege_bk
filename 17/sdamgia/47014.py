numbers = [int(r) for r in open('47014.txt')]
sr_arfm = [r for r in numbers if r % 2 != 0]
sr_arfm = sum(sr_arfm) / len(sr_arfm)

c = m = 0
for idx in range(1, len(numbers)):
    f, s = numbers[idx - 1:idx + 1]

    c1 = (f % 5 == 0 and s < sr_arfm) or (f < sr_arfm and s % 5 == 0)
    if c1:
        c += 1
        m = max(m, f + s)
print(c, m)
