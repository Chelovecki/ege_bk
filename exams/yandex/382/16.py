n = 2*7**2+42*49**49-357

res = ''
while n != 0:
    res += str(n % 7)
    n //= 7
print(res.count('6'))
