c = 0
for r in range(10,21):
    if bin(r)[2:].count('1')> 2:c+=1
print(c)