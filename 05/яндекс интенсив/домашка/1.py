def f(n):
    b=bin(n)[2:]
    if n%3==0:b+=b[-2]+b[-1]
    else: b+= bin((n%3)*3)[2:]
    return  int(b,2)

print(f(9))
print(f(10))
m=10_000
for r in range(1,10_000):
    res = f(r)
    if res>=195:
        m=min(m,res)
print(m)