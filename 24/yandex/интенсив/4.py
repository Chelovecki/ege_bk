s = open('4.txt').read()

c = m = 0

for start_idx in range(3):
    for r in range(start_idx, len(s), 3):
        ay_52 = s[r - 2:r + 1]
        if ay_52 == 'ABA' or ay_52 == 'BAB':
            c += 1

        else:
            m = max(m, c)
            c = 0
    print(m)

print("-" * 20)

s = s.replace('ABA', '*').replace('BAB', '*')

print('*' * 5 in s)
print('*' * 4 in s)
print(len('*' * 4))
