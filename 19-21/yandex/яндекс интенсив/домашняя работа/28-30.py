def f(s1, s2, m):
    if s1 >= 40 or s2 >= 40: return m % 2 == 0
    if m == 0: return 0
    if s1 > s2:
        h = [
            f(s1 + 1, s2, m - 1),
            f(s1 + 2, s2, m - 1),
            f(s1 + 3, s2, m - 1),
            f(s1, s2 * 2, m - 1),
        ]
    if s2 > s1:
        h = [
            f(s1, s2 + 1, m - 1),
            f(s1, s2 + 2, m - 1),
            f(s1, s2 + 3, m - 1),
            f(s1 * 2, s2, m - 1),
        ]
    if s1 == s2:
        h = [
            f(s1 + 1, s2, m - 1),
            f(s1 + 2, s2, m - 1),
            f(s1 + 3, s2, m - 1),
            f(s1, s2 + 1, m - 1),
            f(s1, s2 + 2, m - 1),
            f(s1, s2 + 3, m - 1)
        ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


m = 1_000_000
for s1 in range(1, 40):
    for s2 in range(1, 40):
        if f(s1, s2, 1):
            m = min(m, s1 + s2)
print("19)", m)

print("20)", [r for r in range(1, 40) if not f(11, r, 1) and f(11, r, 3)])
print("21)", [r for r in range(1, 40) if not f(31, r, 2) and f(31, r, 4)])
