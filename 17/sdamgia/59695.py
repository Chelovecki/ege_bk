numbers = [int(r) for r in open('59695.txt')]
m_in_seq = max(r for r in numbers if str(r).endswith('15'))

c = m = 0
for idx in range(2, len(numbers)):
    f = numbers[idx - 2]
    s = numbers[idx - 1]
    t = numbers[idx]

    c1 = len([r for r in [f, s, t] if len(str(r)) == 4]) == 1
    c2 = (f + s + t) >= m_in_seq
    if c1 and c2:
        c += 1
        m = max(m, f + s + t)
print(c, m)
