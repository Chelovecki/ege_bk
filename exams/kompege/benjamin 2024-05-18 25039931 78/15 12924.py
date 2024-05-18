def f(a,x):
    p = list(range(2,20+1,2))
    q = list(range(3,30+1,3))
    return ((x in a) <= (x in p)) and ((x not in q) <= (x not in a))


for a in range(100_000):
    a = list(range(a))
    if all(f(a,x) for x in range(-10_000, 10_000)):
        print(len(a),a)
