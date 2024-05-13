from itertools import permutations

c = 0
b = 0


def l(s:str):
    for glas in 'оеь':
        for neglas in 'свт':
            if  (((glas+glas+neglas+neglas) not in s) and ((neglas+neglas+glas+glas) not in s)):
                return 0
    return 1


for r in permutations('совесть'):
    b += 1
    r = "".join(r)
    c += l(r)

print(c, b)
