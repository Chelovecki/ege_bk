n = (2 ** 2048) + (32 ** 102) - (8 * 4 ** 128)

res = ''
while n != 0:
    div = n % 32
    if n > 9: res += 'A'
    n //= 32
    
print(len(res))
