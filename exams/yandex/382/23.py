import itertools

res = set()
for x1,x2,x3,x4,x5,x6,x7 in itertools.product([0,1],repeat=7):
    for y1,y2,y3,y4,y5,y6,y7 in itertools.product([0,1],repeat=7):
        if (x1<=x2) and (x2<=x3) and (x4<=x5) and (x5<=x6):
            if (y2<=y1) and (y3<=y2) and (y5<=y4) and (y6<=y5):
                if (x3<=y7) or (x7<=y4):
                    res.add((x1,x2,x3,x4,x5,x6,x7,y1,y2,y3,y4,y5,y6,y7))
print(len(res))
