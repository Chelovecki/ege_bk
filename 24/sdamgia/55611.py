import string

total_frequ = dict.fromkeys(string.ascii_uppercase, 0)
for line in open('55611.txt').readlines():
    frequ = dict.fromkeys(string.ascii_uppercase, 0)
    line = line.replace('A', ' ')
    for obj in line.split():
        frequ[obj[0]] += 1
    frequ = sorted(frequ.items(), key=lambda x: x[1])
    max_let = frequ[-1][1]

    for obj in frequ:
        if obj[1] == max_let:
            total_frequ[obj[0]] += 1

print(max(sorted(total_frequ.items(), key=lambda x: x[1])))
#todo