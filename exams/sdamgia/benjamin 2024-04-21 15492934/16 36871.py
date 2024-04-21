def f(n):
    if n==0:return 0
    if n>0 and n%2==0: return f(n/2)
    if n%2!=0:return 1+f(n-1)


c = 0
for r in range(1,1001):
    if f(r) == 3: c+=1
print(c)