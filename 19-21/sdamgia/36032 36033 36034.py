def f(s1, s2, m):
    if s1 + s2 >= 107: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 2, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2 * 2, m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else any(h)


print("19)", [r for r in range(1, 94) if f(13, r, 2) and not f(13, r, 1)][0])


# any ---> all
def f(s1, s2, m):
    if s1 + s2 >= 107: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 2, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2 * 2, m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("20)", [r for r in range(1, 94) if f(13, r, 3) and not f(13, r, 1)])
print("21)", [r for r in range(1, 94) if f(13, r, 4) and not f(13, r, 2)][0])
