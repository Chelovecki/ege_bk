def f(s1, s2, s3, m):
    if s1 + s2 + s3 >= 25 or s1 >= 20 or s2 >= 20 or s3 >= 20: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 * 2, s2, s3, m - 1),
        f(s1, s2 * 2, s3, m - 1),
        f(s1, s2, s3 * 2, m - 1),

        f(s1 + 2, s2 + 2, s3 + 2, m - 1),
    ]

    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)", [r for r in range(1, 20) if not f(2, 3, r, 1) and f(2, 3, r, 2)])
print("20)", [r for r in range(1, 20) if not f(2, 3, r, 1) and f(2, 3, r, 3)])
print("21)", [r for r in range(1, 20) if not f(2, 3, r, 2) and f(2, 3, r, 4)])