def f(a, x, y):
    return (not (x + y > 2 * a)) and (x >= 0) and ((y >= 0) or (abs(x) <= a)) and (abs(y) <= a)


range_xy = range(100)
res = []
for a in range(20):
    flag = True
    for x in range_xy:
        for y in range_xy:
            if f(a, x, y):
                if x * y > 80:
                    res.append(a)
print(min(res))
