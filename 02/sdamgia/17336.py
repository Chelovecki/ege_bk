print('x y z w')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
                if log and z == 0:
                    print(x, y, z, w)

# z == 0, потому что мы нашли строчку 1011, и поняли, что 0 - это z.
# для этого фрагмента табл. истинности z всегда == 0.
# поэтому для удобства
