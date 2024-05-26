def f(a,x):
    b = range(70,81)
    return (x%12==0) and (x in b) and (x%a!=0)

for a in range(1,1000):
    flag = False
    res = sum([f(a,x) for x in range(100_000)])
    if res == 0:
        print(a)