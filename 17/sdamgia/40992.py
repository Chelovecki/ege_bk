numbers = [int(r) for r in open('40992.txt')]
sr_arfm = [r for r in numbers if r%2!=0]
sr_arfm = sum(sr_arfm) / len(sr_arfm)

c = m = 0
for r in range(1, len(numbers)):
    f = numbers[r - 1]
    s = numbers[r]

    c1 = (f % 5 == 0 or s % 5 == 0)
    if c1 and (f < sr_arfm or s < sr_arfm):
        c += 1
        m = max(m, f + s)
print(c, m)
