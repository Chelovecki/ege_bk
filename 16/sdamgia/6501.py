def f(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return f(n - 1) * f(n - 2)


print(f(4))