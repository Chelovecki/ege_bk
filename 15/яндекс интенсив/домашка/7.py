def f(a, x):
    first = [14, 16, 18, 20, 22, 24]
    second = [16, 19, 22, 25, 28]
    return (x not in first) or ((x not in second) <= (x in a))

a=range(1,25)
res = set()
if all(f(a, x) for x in range(-1000, 1000)):
        curr_proizv = 1
        for num in a:
            curr_proizv *= num
        res.add(curr_proizv)
print(min(res))

#todo