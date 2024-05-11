def f(a1,a2,x):
    b = range(34,73)
    c = range(32,61)
    a=range(a1,a2+1)
    return ((x in b) <= (x in a)) and ((not (x in c))or (x in a))

res = set()
for a1 in range(100):
    for a2 in range(a1+1,100):
        if all(f(a1,a2,x) for x in range(1000)):
            res.add(a2-a1)
print(res)