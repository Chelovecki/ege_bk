def f(a, x):
    return (x % 26 != 0 and x % a == 0) <= (x % 39 == 0 or x % a != 0)


for a in range(1, 1000):
    if all([f(a, x) for x in range(1, 10_000)]):
        print(a)
        break
