def f(s, m):
    if s % 10 == 0: return m % 2 == 0
    if m == 0: return 0
    h = [f(s + 1, m - 1), f(s + 3, m - 1), f(s + 11, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)", [r for r in range(11, 99) if not f(r, 1) and f(r, 2)][0])
print("20)", len([r for r in range(11, 99) if not f(r, 1) and f(r, 3)]))
print("21)", sum([r for r in range(11, 99) if not f(r, 2) and f(r, 4)]))
# странная тема, конечно, с 2значным числом
