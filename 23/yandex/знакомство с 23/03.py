def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a + 1, b) + f(a * 2, b)


print(f(3, 6) * f(6, 12) * f(12, 16))
