for r in [128,194,208,64]:
    print(f"{r:08b}",end=' ')
print()

for r in [255,255,224,0 ]:
    print(f"{r:08b}",end=' ')
print()

for r in ['10000000', '11000010', '11000000', '00000000']:
    print(int(r,2), end=' ')