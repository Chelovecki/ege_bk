
def f(n):
    b =bin(n)[2:]
    if sum(map(int,b))%2==0:
        b+='0'
        b = '10'+b[2:]
    else:
        b+='1'
        b = '11'+b[2:]
    return int(b,2)

print(f(6))
print(f(4))


for n in range(1,100_000):
    if f(n) < 35:
        print(n)
