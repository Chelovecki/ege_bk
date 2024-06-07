s = open('7.txt').read()
c=m=0
for r in range(2, len(s)):
 ay_52 = s[r-2:r+1]
 if ay_52[0] in list('ABC'):
     if ay_52[1] in list('CDE'):
         if ay_52[2] not in list('AE'):
             if len(ay_52) == len(set(ay_52)):
                 c+=1
print(c)