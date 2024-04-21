def f(a, x, y):
    return ((x < 6) <= (x ** 2 < a)) and ((y ** 2 <= a) <= (y <= 6))


res = []
xy = 10000
for a in range(100):
    flag = True
    for x in range(xy):
        for y in range(xy):
            if not f(a, x, y):
                flag = False
                break
    if flag: res.append(a)
print(res)
print(len(res))
