from fnmatch import fnmatch
def div(n):
    res = set()
    for delitel in range(1,int(n**0.5)+1):
        if n%delitel == 0:
            res.add(delitel)
            res.add(n//delitel)
        if sum(res)> 2024: return None
    return res

for r in range(10**8):
    if fnmatch('13*7?5', str(r)):
        bebra = div(r)
        # bebra  [r, 1]

        if bebra and sum(bebra)%2024 == 0:
            print(r,max(bebra))

# пиздец какие еще тривиальные делители блять
