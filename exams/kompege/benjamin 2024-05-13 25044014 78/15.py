def f(a,x,y):
    return (99 != y + (2*x)) or (a < x) or (a < y)


for a in range(100):
    if all([f(a,x,y) for x in range(1000) for y in range(1000)]):
        print(a)


