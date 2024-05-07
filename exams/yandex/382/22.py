def f(a, b):
    if a > b or a == 6 or a == 16: return 0
    if a == b: return 1
    return f(a + 1, b) + f(a * 2, b) + f(a + 3, b)


print(f(1, 8) * f(8, 19))
