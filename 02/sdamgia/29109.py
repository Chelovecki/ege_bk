print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log = ((z <= w) or (y == w)) and ((x or z) == y)
                if log and x+y+z+w!=4:
                    print(x, y, z, w)
