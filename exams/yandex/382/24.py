n = int(input())
cnt = 0
p = 1
while n != 0:
    digit = n % 10
    if digit % 2 == 1:
        cnt += 1
        p *= digit
    n //= 10
if p > 1:
    print(p)
else:
    print('NO')