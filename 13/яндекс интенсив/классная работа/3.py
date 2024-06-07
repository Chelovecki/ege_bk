from ipaddress import *

c = 0
for n in ip_network('101.157.240.0/255.255.252.0', 0):
    n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
    left = (n[0] + n[1]).count('1')
    right = (n[2] + n[3]).count('1')
    if left > right: c += 1
print(c)
