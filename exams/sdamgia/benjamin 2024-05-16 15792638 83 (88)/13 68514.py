from ipaddress import *

net = ip_network('122.159.136.144/255.255.255.248', 0)
c = 0
for n in net:
    n = "".join([bin(int(r))[2:].zfill(8) for r in str(n).split('.')])
    if n.count('1') % 4 != 0: c += 1
print(c)
