def f(s1, s2, m):
    if s1 + s2 >= 59: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s1 + 1, s2, m - 1),
        f(s1 * 2, s2, m - 1),
        f(s1, s2 + 1, m - 1),
        f(s1, s2 * 2, m - 1)
    ]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print("19)",[r for r in range(2,53) if f(5,r,1)][0])
print("20)",[r for r in range(2,53) if not f(5,r,1) and f(5,r,3)])
print("21)",[r for r in range(2,53) if not f(5,r,2) and f(5,r,4)][0])