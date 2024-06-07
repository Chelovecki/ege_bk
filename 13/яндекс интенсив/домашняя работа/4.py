from ipaddress import *
c=0
for n in ip_network('235.86.56.0/255.255.248.0',0):
    n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
    if n[-1].endswith('11'):c+=1
print(c)