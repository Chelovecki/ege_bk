print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log = (x == (not y)) <= (z == (y or w))
                if not log and z == 0:
                    print(x, y, z, w)