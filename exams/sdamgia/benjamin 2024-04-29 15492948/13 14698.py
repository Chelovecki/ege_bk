for r in [93, 138, 161, 94]:
    print(f"{r:08b}", end=' ')
print()

for r in [255, 255, ]:
    print(f"{r:08b}", end=' ')
print('11100000', end=' ')

print('00000000', end=' ')

print()
for r in [93, 138, 160, 0]:
    print(f"{r:08b}", end=' ')

print(f"\nполучается, что {'00000 00000000'.count('0')}")
