def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a + 2, b) + f(a * a, b) + f(a ** 3, b)


print(f(10, 1000))
