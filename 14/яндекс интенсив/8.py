m=0
for x in '0123456789abcdef'.upper():
    for y in '0123456789abcdef'.upper():
        n = int(f'27A{x}23',16) + int(f'8{y}E5D2',16)
        if n%5==0:
            m = max(int(x,16) + int(y,16),m)
print(m)