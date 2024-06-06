from fnmatch import *
c=m=0
for r in range(408015016023,10**12):
    if fnmatch(str(r), '4?8?15?16?23'):
        if r%123==42:
            c+=1
            m=max(m,r)
            print(c,r)
print(c,m)
