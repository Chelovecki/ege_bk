import ipaddress
c=0
for net in ipaddress.ip_network('142.68.56.0/255.255.255.240', 0):
    net = [bin(int(r))[2:].zfill(8) for r in str(net).split('.')]
    if (net[0]+net[1]).count('1') < (net[2]+net[3]).count('1'):
        print(net)
        c+=1
print(c)