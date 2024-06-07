c=m=0
for a1 in range(10):
    for a2 in range(10):
        for a3 in range(10):
            for a4 in range(10):
                r = int(f'4{a1}8{a2}15{a3}16{a4}23')
                if r % 123 == 42:
                    c += 1
                    m = max(m, r)
print(c, m)
