s = open('24_10724.txt').read()

# потому что с 71-го начинаются числа, которые не входят в 16сс.
for acsii_symb in range(71, 91):
    print(chr(acsii_symb), end='')
print()
print(len(s))

for acsii_symb in range(71, 91):
    s = s.replace(chr(acsii_symb), " ")

res = set()

for sequence in s.split():
    while sequence[0] == '0':
        sequence = sequence[1:]
    res.add(len(sequence))
print(max(res))