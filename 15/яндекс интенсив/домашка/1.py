def f(x, y):
    return (2 * y > 5 * x) or (x * y < a) or (x >= 22)


for a in range(10_000):
    if all(f(x, y) for x in range(100) for y in range(100)):
        print(a)
        break
