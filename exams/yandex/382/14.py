s = 40 * '1'
while '1111' in s:
    if '222' in s:
        s = s.replace('22', '1', 1).replace('11111', '3', 1)
    else:
        s = s.replace('33', '1', 1).replace('11111', '2', 1)
print(s)
