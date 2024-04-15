def f(a,m):
    if a>=301: return m%2==0
    if m==0:return 0
    h = [
        f(a+3, m-1),
        f(a*5,m-1)
    ]
    return any(h) if m%2!=0 else all(h)

print("19)", [r for r in range(1,301) if not f(r,1) and f(r,2)][0])
print("20)", [r for r in range(1,301) if not f(r,1) and f(r,3)][:2])
print("21)", [r for r in range(1,301) if not f(r,2) and f(r,4)][0])