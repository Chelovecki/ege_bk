print('x y z w')

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log = ((w<=x)or(y<=z)) and ((x==y)<=(w==z))

                if not log and w==1:
                    print(x,y,z,w)
