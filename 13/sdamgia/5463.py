[print(f'{x:b}'.zfill(8), end=' ') for x in [64, 128, 194, 208]]
print()
[print(f'{x:b}'.zfill(8), end=' ') for x in [255, 255, 224, 0]]

print()
[print(int(r, 2), end=' ') for r in ['01000000', '10000000', '11000000', '00000000']]
