max_posib_len = list()

for r in range(3, 1001):
    s = '1' + '2' * r
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)

        if '322' in s:
            s = s.replace('322', '21', 1)

        if '222' in s:
            s = s.replace('222', '3', 1)

    max_posib_len.append(len(s))
print(max(max_posib_len))
