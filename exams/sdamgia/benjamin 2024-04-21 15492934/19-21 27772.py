def f(c1, c2, m):
    if c1 + c2 <= 20: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(c1 - 1, c2, m - 1),
        f(c1, c2 - 1, m - 1)
    ]
    if c1 % 2 == 0:
        h.append(f(c1 // 2, c2, m - 1))
    else:
        h.append(f((c1 - 1) // 2, c2, m - 1))

    if c2 % 2 == 0:
        h.append(f(c1, c2 // 2, m - 1))
    else:
        h.append(f(c1, (c2 - 1) // 2, m - 1))

    return any(h) if m % 2 != 0 else any(h)


print("19)", [r for r in range(10, 50) if not f(10, r, 1) and f(10, r, 2)][-1])

# после 19-го задания переписываем фукнцию так, чтобы было использовано all в return
def f(c1, c2, m):
    if c1 + c2 <= 20: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(c1 - 1, c2, m - 1),
        f(c1, c2 - 1, m - 1)
    ]
    if c1 % 2 == 0:
        h.append(f(c1 // 2, c2, m - 1))
    else:
        h.append(f((c1 - 1) // 2, c2, m - 1))

    if c2 % 2 == 0:
        h.append(f(c1, c2 // 2, m - 1))
    else:
        h.append(f(c1, (c2 - 1) // 2, m - 1))

    return any(h) if m % 2 != 0 else all(h)


print("20)", "".join([str(r) for r in range(10, 500) if not f(10, r, 1) and f(10, r, 3)]))
print("20)", [r for r in range(10, 500) if not f(10, r, 2) and f(10, r, 4)])
