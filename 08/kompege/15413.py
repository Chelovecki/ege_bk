def to_9(n):
    res = ''
    while n != 0:
        res += str(n % 9)
        n //= 9
    return res[::-1]


c = 0
for r in range(100, 10_000):
    res = to_9(r)

    if len(res) == 4:
        if res.count('8') == 1:
            left = sum([int(b) for b in res[0:res.index('8')]])
            right = sum([int(b) for b in res[res.index('8') + 1:1000]])
            if left == right: c += 1
print(c)
