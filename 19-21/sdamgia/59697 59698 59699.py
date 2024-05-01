def f(s, m):
    if s >= 88: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 4, m - 1),
        f(s * 3, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [r for r in range(2, 87) if not f(r, 1) and f(r, 2)])
print('20)', [r for r in range(2, 87) if not f(r, 1) and f(r, 3)])
print('21)', [r for r in range(2, 87) if not f(r, 2) and f(r, 4)])
