def f(a, b):
    if a > b or a == 33: return 0
    if a == b: return 1
    return f(a + 1, b) + f(a * 2, b) + f(a * a, b)


print(f(8, 32) * f(32, 115))
