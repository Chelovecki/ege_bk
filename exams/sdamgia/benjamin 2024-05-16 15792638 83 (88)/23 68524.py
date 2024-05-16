def f(a, b, flag):
    flag.append(a)
    if a > b: return 0
    if a == b and 11 in flag and 13 in flag: return 1
    return f(a + 1, b, flag) + f(a + 2, b, flag) + f(a * 2, b, flag)


print(f(4, 15, []))