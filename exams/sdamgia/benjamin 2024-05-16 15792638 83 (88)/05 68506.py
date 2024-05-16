def f(n):
    b = bin(n)[2:]
    if n%2==0: b= '10' +b
    else: b = '1' + b + '01'
    return int(b,2)

# print(f(4))
# print(f(5))


for n in range(10000):
    if f(n) > 516:
        print(n)
        break