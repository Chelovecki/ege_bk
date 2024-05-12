stepen_dvoiki = [2**r for r in range(14)]

for x in range(8):
    res = int(f"{x}1{x}",16) + int(f"{x}3{x}3",8)
    if res in stepen_dvoiki:
        print(x)