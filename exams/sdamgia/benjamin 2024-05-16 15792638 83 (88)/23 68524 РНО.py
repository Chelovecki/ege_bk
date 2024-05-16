def f(a, b, flag):
    if a > b: return 0
    if a == 13: flag += 1_000_000_000
    if a == 11: flag += 1
    if a == b and flag == 1_000_000_001: return 1
    return f(a + 1, b, flag) + f(a + 2, b, flag) + f(a * 2, b, flag)


print(f(4, 15, 0))


def f(a, b):
    if a > b: return 0
    if a == b: return 1
    return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)


print(f(4, 11) * f(11, 13) * f(13, 15))
