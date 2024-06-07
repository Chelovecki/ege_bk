def f(a, x, y):
    return ((2 * y) > (5 * x)) or ((x * y) < a) or (x >= 22)


for a in range(10_00000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not f(a, x, y):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(a)
