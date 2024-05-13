def f(a,b):
    if a>b or a==12:return 0
    if a==b:return 1
    return f(a+1,b)+f(a+2,b)+f(a*2,b)

print(f(2,9)*f(9,17))