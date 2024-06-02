def f(s1, s2, m):
    if s1 == s2: return m % 2 == 0
    if m == 0: return 0
    if s1 > s2:
        h = [f(s1, s2 + 1, m - 1), f(s1, s2 + 3, m - 1)]
    if s2 > s1:
        h = [f(s1 + 1, s2, m - 1), f(s1 + 3, s2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)", [r for r in range(1, 24) if not f(13, r, 1) and f(13, r, 2)])
print("20)", [r for r in range(1, 24) if not f(13, r, 1) and f(13, r, 3)][:2])
print("21)", [r for r in range(1, 24) if not f(13,r, 2) and f(13,r, 4)],"- отсюда он может выиграть вторым ходом")
print([r for r in range(1,24) if f(13,r,3)], "- отсюда выигрывает петя")
