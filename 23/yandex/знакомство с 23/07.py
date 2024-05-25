def f(a, b):
    if a > b or a == 11: return 0
    if a == b: return 1
    return f(a + 1, b) + f(a + 4, b) + f(a * 3, b)


print(f(7, 27) * f(27, 42))
