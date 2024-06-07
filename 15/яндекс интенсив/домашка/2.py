def f(a, x, y):
    return (x + 2 * y != 58) or ((a - x > 0) == (a + y > 0))


for a in range(10_000):
    if all(f(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break
