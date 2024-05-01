def f(s, m):
    if s >= 28: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 3, m - 1),
        f(s * 2, m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else any(h)


print("19)", [r for r in range(1, 28) if f(r, 2) and not f(r, 1)][0])


def f(s, m):
    if s >= 28: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 3, m - 1),
        f(s * 2, m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("20)", [r for r in range(1, 28) if f(r, 3) and not f(r, 1)])
print("21)", [r for r in range(1, 28) if f(r, 4) and not f(r, 2)][0])
