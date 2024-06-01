from fnmatch import fnmatch
def div(n):
    res = set()
    for delitel in range(1,int(n**0.5)+1):
        if n%delitel == 0:
            if delitel!=1 and delitel!=n:
                res.add(delitel)
                res.add(n//delitel)
    return res

for r in range(10**8):
    if fnmatch(str(r), '13*7?5'):
        if (r+1) / 2024==0:
            print(r, max(div(r)))

# пиздец какие еще тривиальные делители блять
#todo РНО