def div(n):
    res = set()
    for r in range(1,int(n**0.5)+1):
        if n%r==0:
            res |= {r,n//r}
    return res

# print(div(21))

for r in range(123456, 987654+1):
    a = div(r)
    if len(set(a)) == 5:
        a = sorted(a)
        print(a[-2], a[-1])