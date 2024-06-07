from ipaddress import *
c=0
for n in ip_network('192.168.32.160/255.255.255.240',0):
    n="".join([bin(int(r))[2:].zfill(8) for r in str(n).split('.')])
    if n.count('0') > 21: c+=1
print(c)