def f(a,x):
    p = list(range(2,20+1,2))
    q = list(range(3,30+1,3))
    return ((x in a) <= (x in p)) and ((x not in q) <= (x not in a))

b = []
for a1 in range(100):
    for a2 in range(a1+1,100):
        a = list(range(a1,a2))
        if all(f(a,x) for x in range(32)):
            b.append(len(a))
print(b)
