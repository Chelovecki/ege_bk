from ipaddress import *

for mask in range(31):
    adres1=  ip_address('118.187.59.255')
    adres2=  ip_address('118.187.65.115')
    net1 = ip_network(f'118.187.59.255/{mask}',0)
    net2 = ip_network(f'118.187.65.115/{mask}',0)
    if net1[0] < adres1 < net1[-1] and net2[0] < adres2 < net2[-1]:
        print(net1,net2,mask)


# неочевидно... мува не понял