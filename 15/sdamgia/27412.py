def f(x, y): return x % y == 0


for a in range(1, 1000000):
    flag = True
    for x in range(1, 100000):
        log_f = (not f(x, a)) <= (f(x, 6) <= (not f(x, 9)))
        if not log_f:
            flag = False
            break
    if flag: print(a)
