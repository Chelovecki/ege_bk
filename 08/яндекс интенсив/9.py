from itertools import product
c=0
for r in product('01234567',repeat=5):
    if r[0]!='0':
        r="".join(r)
        if r.count('1') == 0 and len(r) == len(set(r)):
            for b in '246':r=r.replace(b,'0')
            for b in '1357':r=r.replace(b,'1')
            if '00' not in r and '11'not in r:
                c+=1
print(c)
