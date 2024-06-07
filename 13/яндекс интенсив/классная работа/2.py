from ipaddress import *

c = 0
for n in ip_network('87.226.26.72/255.255.255.252', 0):
    n = "".join([bin(int(r))[2:].zfill(8) for r in str(n).split('.')])
    if n.count('0') % 2 == 0: c += 1
print(c)
