def f(a, x):
    return ((x % 12 == 0) and (x & 4 == 0)) <= (x + 1 > a)


for a in range(1,100):
    if all(f(a, x) for x in range(120_000)):
        print(a)
