from itertools import permutations

res = set()
for r in permutations('носочечки'):
    r = "".join(r)
    word_to_add = r
    for sogl in 'нсчк':
        r = r.replace(sogl, '1')
    for glas in 'оеи':
        r = r.replace(glas, '0')
    flag = True
    for id in range(1, len(r)):
        if r[id - 1] == r[id]:
            flag = False
            break
    if flag:
        res.add(word_to_add)
print(len(res))
