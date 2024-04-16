# 7354
def f(a, m):
    if a >= 31: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a + 1, m - 1),
        f(a + 5, m - 1),
        f(a * 2, m - 1)
    ]
    return any(h) if m % 2 != 0 else any(h)


print("19)", [r for r in range(1, 31) if not f(r, 2) and f(r, 3)][0])


# переписываю функцию после изменения под фразу "после неудачного хода"
def f(a, m):
    if a >= 31: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a + 1, m - 1),
        f(a + 5, m - 1),
        f(a * 2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)


print("20)", len([r for r in range(1, 31) if not f(r, 1) and f(r, 999)]))
print("21)", [r for r in range(1, 31) if not f(r, 4) and f(r, 6)][0])
