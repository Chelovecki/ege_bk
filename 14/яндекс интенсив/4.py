def to_15(n):
    res = ''
    while n != 0:
        ay = n % 15
        if ay == 10:
            res += 'A'
        elif ay == 11:
            res += 'B'
        elif ay == 12:
            res += 'C'
        elif ay == 13:
            res += 'D'
        elif ay == 14:
            res += 'E'
        else:
            res += str(ay)
        n //= 15
    return res[::-1]


n = (3 * 15 ** 1140) + (2 * 15 ** 1025) + (15 ** 923) - (3 * 15 ** 85) + (2 * 15 ** 74) + 3
n = to_15(n)
# print(n)
c = m = 1
for idx in range(1, len(n)):
    if n[idx - 1] == n[idx]:
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)
