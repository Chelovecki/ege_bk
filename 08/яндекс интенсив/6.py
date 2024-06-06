from itertools import product
c=0
for r in product('0123456789abcd', repeat=5):
    if r[0]!='0':
        r = "".join(r)
        for lett in 'abcd':
            r=r.replace(lett, 'a')
        for num in'13579':
            r=r.replace(num,'1')
        if 'a1' not in r and '1a' not in r:
            c+=1
print(c)