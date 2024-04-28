from itertools import *

def f(x,z,y,w):
    return (x<=(y==w)) and (y==(w<=z))

for a1,a2 in product([0,1], repeat=2):
    t = [
        (1,a1,0,1),
        (0,0,a2,0),
        (0,0,0,1)
    ]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p,r))) for r in t] == [1,1,0]:
            print(*p,sep='')