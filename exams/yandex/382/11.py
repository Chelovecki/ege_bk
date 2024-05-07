def F(n):
    if n <= 8:
        F(n + 3)
    if n < 10:
        print(n,end="")
    if n <= 5:
        F(n + 4)
F(1)