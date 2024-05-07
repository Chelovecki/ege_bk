s = open('24_14643.txt').read()

print(max(len(r) for r in s.replace('AXMM', 'AXM XMM').split(' ')))
