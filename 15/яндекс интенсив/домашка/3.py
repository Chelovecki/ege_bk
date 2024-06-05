def f(a,x):
    return (x&a==0) or ((x&44==4) <= (x&27==10))

for a in range(1000):
    if all(f(a,x) for x in range(10_000)):
        print(a)