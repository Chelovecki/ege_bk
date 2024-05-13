from itertools import  *
c=0
for n,r  in enumerate(product(sorted('пятница'), repeat=6),1):
    if n % 2 == 0:
        if r[0] != 'н':
            r = "".join(r)
            if r.count('я') == 2:
                c += 1
print(c)
