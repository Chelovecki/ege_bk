def f(a, b):
    if a > b or a == 20: return 0
    if a == b: return 1
    return f(a + 1, b) + f(a + 3, b) + f(a ** 2, b)


print(f(3, 23) * f(23, 25))
