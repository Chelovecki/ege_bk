s = open('2420.txt').read()

s = s.replace('C', " ").replace("D", ' ')

print(max(len(r) for r in s.split()))