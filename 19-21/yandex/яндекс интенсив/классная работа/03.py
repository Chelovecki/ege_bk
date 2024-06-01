def f(s1,s2,m):
    if s1+s2>=68: return m%2==0
    if m==0:return 0
    h = [
        f(s1+1,s2,m-1),
        f(s1+s2,s2,m-1),
        f(s1,s2+1,m-1),
        f(s1,s2+s1,m-1)
    ]
    return any(h) if (m-1)%2==0 else any(h)


print("19)", [r for r in range(1,60) if f(8,r,2)][0])

def f(s1,s2,m):
    if s1+s2>=68: return m%2==0
    if m==0:return 0
    h = [
        f(s1+1,s2,m-1),
        f(s1+s2,s2,m-1),
        f(s1,s2+1,m-1),
        f(s1,s2+s1,m-1)
    ]
    return any(h) if (m-1)%2==0 else all(h)


print("20)", [r for r in range(1,60) if not f(8,r,1) and f(8,r,3)])
print("21)", [r for r in range(1,60) if not f(8,r,2) and f(8,r,4)])