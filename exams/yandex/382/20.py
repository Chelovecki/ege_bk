res = []
for x in range(20000):
    x_copy = x
    a, b = 0, 0
    while x > 5:
        if x % 5 < 2:
            a += 1
        if x % 5 > 2:
            b += 1
        x //= 5
    if a == 2 and b == 2:
        res.append(x_copy)
print(min(res))
