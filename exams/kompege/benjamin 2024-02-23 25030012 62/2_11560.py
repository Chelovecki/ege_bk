print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log_ = (x or (not y)) and (not (x == z)) and w
                if log_:
                    print(x,y,z,w)
print("\nответ zyxw")
