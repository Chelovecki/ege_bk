from ipaddress import *

for a in range(256):
    net = ip_network(f'248.112.{a}.35/255.255.255.240', 0)
    flag = True
    for n in net:
        n = [bin(int(r))[2:].zfill(8) for r in str(n).split('.')]
        if not ((n[0] + n[1]).count('0') <= (n[2] + n[3]).count('0')):
            flag = False
            break
    if flag:
        print(a)
