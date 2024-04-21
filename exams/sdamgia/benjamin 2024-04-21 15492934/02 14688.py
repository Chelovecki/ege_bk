print("x y z")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            log_ = (x or y) <= (z==x)
            if not log_:
                print(x,y,z)
