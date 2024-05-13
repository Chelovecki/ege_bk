from ipaddress import *


def b(adr: str):
    adr = [int(r) for r in adr.split('.')]
    adr = [bin(r)[2:].zfill(8) for r in adr]
    return adr[2].count('0') > adr[3].count('0')


c = 0
for a in range(256):
    ip = f"246.81.65.{a}"
    net = ip_network(f"{ip}/255.255.255.224", 0)
    if ip not in [str(net.broadcast_address), str(net.network_address)]:
        if all(b(str(n)) for n in net.hosts()):
            c += 1
print(c)
