from ipaddress import *


def b(adr: str):
    adr = [int(r) for r in adr.split('.')]
    adr = [bin(r)[2:].zfill(8) for r in adr]
    print(adr)
    return adr[2].count('0') > adr[3].count('0')


c = 0
for a in range(256):
    net = list(map(str, ip_network(f"246.81.65.{a}/255.255.255.224", 0).hosts()))
    print(net)
    if all(b(n) for n in net):
        c += 1
print(c)
