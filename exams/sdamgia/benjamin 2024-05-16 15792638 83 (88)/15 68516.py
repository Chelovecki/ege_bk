def f(a, x):
    return (not (x % a == 0)) <= ((x % 14 == 0) <= (not (x % 4 == 0)))


for a in range(1, 100):
    if all([f(a, x) for x in range(1, 10_000)]):
        print(a)
