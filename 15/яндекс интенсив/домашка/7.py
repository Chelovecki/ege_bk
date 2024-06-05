def f(a1,a2,x):
    return (x not in [14,16,18,20,22,24]) or ((x not in [16,19,22,25,28]) <= x in range(a1,a2))


m = 1e+100

for a1 in range(1000):
    for a2 in range(a1,1000):
        if all([f(a1,a2,x) for x in range(1000)]):
            curr_proizv  =1
            for num in range(a1,a2):
                curr_proizv*=num
            m=min(m,curr_proizv)
print(m)
