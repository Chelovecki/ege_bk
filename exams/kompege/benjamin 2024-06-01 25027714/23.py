def f(a, b, usage):
    if a > b: return 0
    if a == b and usage.endswith('BAB'): return 1
    return f(a + 1, b, usage + 'A') + f(a * 2, b, usage + 'B') + f(a + 5, b, usage + 'C')


print(f(5, 62, ''))

# надо просто подождать
