def f(s1, s2, m):
    if s1 + s2 >= 503: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 3, s2, m - 1),
        f(s1, s2 + 3, m - 1),

        f(s1 * 2, s2, m - 1),
        f(s1, s2 * 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else any(h)


print("19)", [r for r in range(1, 488) if not f(15, r, 1) and f(15, r, 2)][0])


def f(s1, s2, m):
    if s1 + s2 >= 503: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 3, s2, m - 1),
        f(s1, s2 + 3, m - 1),

        f(s1 * 2, s2, m - 1),
        f(s1, s2 * 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("20)", [r for r in range(1, 488) if not f(15, r, 1) and f(15, r, 3)])
print("21)", [r for r in range(1, 488) if not f(15, r, 2) and f(15, r, 4)][-1])
