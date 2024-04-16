s = open('24_1975.txt').read()

# странно, что не " "
s = s.replace('PP', "P P")

print(max(len(r) for r in s.split()))
