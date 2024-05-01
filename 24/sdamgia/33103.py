c =0
for line in open('33103.txt').readlines():
    if line.count('A') > line.count('E'): c+=1
print(c)