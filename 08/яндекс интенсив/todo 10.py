from  itertools import permutations
res =set()
for r in set(permutations('носочечки')):
    r = "".join(r)
    new_r =''
    for symb in r:
        if symb in 'счк':r=r.replace(symb, 'н')
        r=r.replace('е', 'о')
    if 'нн' not in r and "оо" not in r:
        res.add(r)
print(len(res))