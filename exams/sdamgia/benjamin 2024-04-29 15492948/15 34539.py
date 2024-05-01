def f(x, a):
    p = range(22, 73)
    q = range(42, 103)
    return not ((not (x in a)) and (x in p)) or (x in q)


res = set()
for a1 in range(50):
    for a2 in range(a1 + 1, 50):
        a = range(a1, a2 + 1)
        flag = True
        for x in range(100_000):
            if not f(x, a):
                flag = False
                break
        if flag:
            res.add(len(a))
            print(a, len(a))
print(min(res))
