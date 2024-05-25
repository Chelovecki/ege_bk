def f(a, b):
    if a < b or a == 22: return 0
    if a == b: return 1
    return f(a - 2, b) + f(a // 2, b) + f(a // 3, b)


print(f(40, 2))
