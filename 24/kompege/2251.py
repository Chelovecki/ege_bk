s = open('24_2251.txt').read()

temp_s = ''
res = []

for r in range(len(s)):
    if temp_s.count('D') <= 2:
        temp_s += s[r]
    else:

        res.append(len(temp_s))
        temp_s = s[r]
print(max(res))

#todo