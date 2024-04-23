print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log = ((not x or z) == (y and (not w))) <= (z and y)

                if not log and x!=0:
                    print(x, y, z, w)
