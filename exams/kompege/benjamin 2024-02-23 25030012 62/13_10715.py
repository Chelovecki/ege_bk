import ipaddress

net = '192.168.32.160/255.255.255.240'
c = 0
for r in ipaddress.ip_network(net, 0):
    r = [bin(int(part))[2:] for part in str(r).split('.')]
    print(r, [part.count('0') for part in r])
    if sum([part.count('0') for part in r]) > 21:
        print(r)
        c += 1
print(c)

# мне не нравится такой ответ ну как видно, там много где есть [6,5,5,5], откуда получается 21, а нужны числа, больше 21
