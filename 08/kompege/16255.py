from itertools import product
c = 0
for r in product(range(9), repeat=7):
    if r[0]!=0 and r[0]%2==0 and r[-1]%3!=0 and r.count(6)>=1:
        c+=1

print(c)
