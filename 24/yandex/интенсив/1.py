s = open('1.txt').read()
s = s.replace('IT', 'I T').replace('TI', 'T I')

s = s.split()

print(max(len(r) for r in s))
