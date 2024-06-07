from itertools import product
c=0
for r in product('этан', repeat=5):
    r = "".join(r)
    if r.count('э') + r.count("а") == 1:
        c+=1
print(c)
