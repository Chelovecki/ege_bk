def f(a1, a2, a3, m):
    if a1 + a2 + a3 >= 25: return m % 2 == 0
    if m == 0: return 0

    h = [
        f(a1 * 2, a2, a3, m - 1),
        f(a1, a2 * 2, a3, m - 1),
        f(a1, a2, a3 * 2, m - 1),
        f(a1 + 2, a2 + 2, a3 + 2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)


print("19)", [r for r in range(1, 20) if not f(2, 3, r, 1) and f(2, 3, r, 2)])
print("20)", [r for r in range(1, 20) if not f(2, 3, r, 1) and f(2, 3, r, 3)][:2])
print("21)", [r for r in range(1, 20) if not f(2, 3, r, 2) and f(2, 3, r, 4)][0])
