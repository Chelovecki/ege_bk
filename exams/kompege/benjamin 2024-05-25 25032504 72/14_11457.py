def to_5(n):
    res = ''
    while n!=0:
        res+=str(n%5)
        n//=5
    return res

for x in range(10_000):
    n = (4*625**1920) + (4*125**x) - (4*25**1940) - (3*5**1950) - 1960
    if to_5(n).count('0') == 1891:
        print(x)
        break