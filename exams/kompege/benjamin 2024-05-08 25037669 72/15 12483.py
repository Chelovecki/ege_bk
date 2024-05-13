def f(a,x):
    return ( not( (x&79) == 0 )) and ( (x&31) == 0 ) <= (not( (x&a) == 0 ))

for a in range(1000):
    if all(f(a,x) for x in range(90,101)):
        print(a)
        break
