from ipaddress import *

c = 0
for n in ip_network('171.128.0.0/255.128.0.0', 0):
    n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
    if (n[0] + n[1]).count('1') < (n[2] + n[3]).count('1'): c += 1
print(c)
