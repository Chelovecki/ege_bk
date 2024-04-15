def f(a, b, m):
    if a * b >= 777: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a + 3, b, m - 1),
        f(a * 2, b, m - 1),
        f(a, b + 3, m - 1),
        f(a, b * 2, m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else any(h)


print("19)", min([r for r in range(1, 111) if f(7, r, 2)]))


# дальше я переписал функцию, так как для 19-го задания надо поменять all на any
def f(a, b, m):
    if a * b >= 777: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a + 3, b, m - 1),
        f(a * 2, b, m - 1),
        f(a, b + 3, m - 1),
        f(a, b * 2, m - 1),
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


a = [r for r in range(1, 111) if not f(7, r, 1) and f(7, r, 3)]
print("20)", a[0], a[-1])

print("21)", min([r for r in range(1, 111) if not f(7, r, 2) and f(7, r, 4)]))
