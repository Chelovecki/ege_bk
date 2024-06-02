def f(s, m):
    if s >= 41: return m % 2 == 0
    if m == 0 or s > 50: return 0
    h = [
        f(s + 1, m - 1),
        f(s + 2, m - 1),
    ]
    if s * 2 <= 50: h.append(f(s * 2, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [r for r in range(1, 41) if f(r, 4) and not f(r, 2)])
print('20)', [r for r in range(1, 41) if not f(r, 2) and not f(r, 4) and f(r, 6)])
print('21)', [r for r in range(1, 41) if not f(r, 1) and f(r, 3)])
print([r for r in range(1, 41) if f(r, 2)])
# ну а дальше "руками, брат" находим, что это значение - 19,
# так как из него можно попасть в 20 и 38, и откуда можно попасть в 41+
