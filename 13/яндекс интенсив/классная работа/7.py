from ipaddress import *

for mask in range(31):
    net = ip_network(f'208.207.230.65/{mask}', 0)
    if str(net.network_address) == '208.207.224.0':
        print(mask)
