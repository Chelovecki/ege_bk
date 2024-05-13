print("y z x w | f g")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                log_f = int((x or (not y)) and (not (x == z)) and w)
                log_g = int((x <= y) and (y <= z) and (z <= w))
                if log_f or log_g:
                    print(z,y,x,w,"|",log_f,log_g)

# и типо можно сверить таблицу что вывелась с тем, что в задании