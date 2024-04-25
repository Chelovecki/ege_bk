numbers = [int(r) for r in open('37344.txt')]
m_in_seq = max(r for r in numbers if r % 15 == 0)

c = m = 0
for idx_f in range(len(numbers)):
    for idx_s in range(idx_f+1, len(numbers)):
        f = numbers[idx_f]
        s = numbers[idx_s]

        if (f * s) % 10 == 0:
            c += 1
            m = max(m, f + s)
print(c, m)
