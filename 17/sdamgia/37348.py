numbers = [int(r) for r in open('37348.txt')]

c = m = 0
for id_f in range(len(numbers)):
    for id_s in range(id_f + 1, len(numbers)):
        f = numbers[id_f]
        s = numbers[id_s]

        if (f * s) % 34 != 0:
            c += 1
            m = max(m, f + s)
print(c, m)
