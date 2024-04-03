"""
№ 10112 (Уровень: Базовый)

(С. Чайкин) В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному  адресу узла и маске сети.

Два узла, находящиеся в одной сети, имеют IP-адреса 92.149.25.164 и 92.149.37.2. Укажите наибольшую возможную сумму байтов маски сети. В ответе укажите только число.
"""

ip1 = [f"{x:08b}" for x in [92, 149, 25, 164]]
ip2 = [f"{x:08b}" for x in [92, 149, 37, 2]]
print(*ip1)
print(*ip2)
# так как ip в 1 сети, то у них первые k бит будет одинаковы.
# значит нам надо печатать единички пока биты в айпи1 и айпи2 равны.
# как только появляется различие - флаг в отрицание и печатаем единички
flag = True
mask = ''

for a, b in zip(ip1, ip2):
    bait = ""
    # это байты в ip адресе
    for a1, b2 in zip(a, b):
        # это биты в байтах
        if a1 == b2 and flag:
            bait += "1"
        else:
            flag = False
            bait += '0'

    mask += bait + " "
print(mask)

print(mask.count('1'))

# а 18 эт о 2 байта  и 2 бита, то есть ответ:
print(int('11111111', 2) + int('11111111', 2) + int('11000000', 2))
