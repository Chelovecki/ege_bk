from ipaddress import *
ip1 = ip_address('151.172.115.121')
ip2 = ip_address('151.172.115.156')
for mask in range(31):

    net1 = ip_network(f'151.172.115.121/{mask}', 0)
    net2 = ip_network(f'151.172.115.156/{mask}', 0)
    if net1[0] < ip1 < net1[-1] and net2[0] < ip2 < net2[-1] and net2!=net1:
        print(net1, net2, mask)
