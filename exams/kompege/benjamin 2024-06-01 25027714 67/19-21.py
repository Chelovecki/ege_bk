def f(s, m):
    if s >= 72: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 3, m - 1),
        f(s + 5, m - 1),
        f(s * 2, m - 1)
    ]
    return all(h) if (m - 1) % 2 == 0 else any(h)


print("19)", [r for r in range(1, 72) if not f(r, 1) and f(r, 2)][0])
print("20)", [r for r in range(1, 72) if not f(r, 1) and f(r, 3)])
print("21)", [r for r in range(1, 72) if not f(r, 2) and f(r, 4)][-1])
