
def F(x):
    return abs(9 - (x - 3) * (x - 3)) - 2

a, b = -10, 10
M, R = a, F(a)
for t in range(a, b + 1):
    if F(t + 1) <= R:
        M, R = t, F(t)
print(M - R)