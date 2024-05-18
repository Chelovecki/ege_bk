from ipaddress import *
c=0
for n in ip_network('136.36.240.16/255.255.255.248',0):
    n = "".join([bin(int(r))[2:].zfill(8) for r in str(n).split('.')])
    if '101' not in n:
        print(n)
        c+=1
print(c)