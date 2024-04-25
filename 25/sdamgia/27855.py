def div(x):
    res = set()
    for d in range(1, int(x**0.5)+1):
        if x%d==0:
            res|={d,x//d}
    return sorted(res)


for r in range(95632, 95700+1):
    res = [r for r in div(r) if r%2==0]
    if len(res) == 6:
        print(res)