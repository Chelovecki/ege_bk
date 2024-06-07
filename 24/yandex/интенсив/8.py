s = open('8.txt').read()
m=len(s)
c=l=0
for r in range(len(s)):
    if s[r]=='E':c+=1
    while c==100:
        m=min(m,r-l+1)
        if s[l]=='E':c-=1
        l+=1
print(m)