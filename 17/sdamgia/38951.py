numbers = [int(r) for r in open('38951.txt')]
m_in_seq = max(r for r in numbers if r % 15 == 0)

c = m = 0
for idx in range(1, len(numbers)):
    f = numbers[idx - 2]
    s = numbers[idx - 1]

    c1 = any([f % 3 == 0, s % 3 == 0])
    if c1 and (f + s) % 5 == 0:
        c += 1
        m = max(m, f + s)
print(c, m)
