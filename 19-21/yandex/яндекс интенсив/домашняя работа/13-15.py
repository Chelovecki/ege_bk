def f(s, m):
    if s >= 22: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 2, m - 1)
    ]
    if s % 2 != 0: h.append(f(s * 2, m - 1))

    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)", [r for r in range(1,22) if not f(r,2) and f(r, 4)])
print("20)", [r for r in range(1,22) if not f(r,1) and f(r, 3)])
print("21)", [r for r in range(1,22) if not f(r,1) and not f(r, 3) and f(r,5)])
