from ipaddress import *

c = 0
for n in ip_network('112.208.0.0/255.255.128.0', 0):
    n = "".join([bin(int(r))[2:].zfill(8) for r in str(n).split('.')])
    if n.count('1') % 11 == 0: c += 1
print(c)
