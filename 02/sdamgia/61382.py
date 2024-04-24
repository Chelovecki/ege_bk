print('x y z w')

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log1 = (w == x) and (y<=z)
                log2 = (w<=x) <= (y==z)
                if log1:
                    print(x,y,z,w)
