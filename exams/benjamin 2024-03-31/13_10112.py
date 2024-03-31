from ipaddress import *

res = []
for mask in range(33):
    net1 = ip_network(f'92.149.25.164/{mask}', 0)
    net2 = ip_network(f'92.149.37.2/{mask}', 0)
    if net1 == net2:
        res.append(f"{mask:08b}".count('1'))
print(max(res))
