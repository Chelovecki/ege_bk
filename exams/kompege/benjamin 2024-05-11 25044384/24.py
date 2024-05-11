import itertools

s = open('24.txt').read()
s = 'D021AB320'
for r in 'ABCDE':
    s=s.replace(r,' ')
s=s.replace('3', ' ').replace('4',' ')

# for obj in s.split():
#     print(obj)
#     input()
c = 0
for obj in s.split():
    if obj[0] =='0':
        obj = obj[1:]
    print(obj)
    for l in range(1,len(obj)+1):
        s = [r for r in itertools.permutations(obj, l) if r[0]!='0']
        print(s)
        c+=len(s)

print(c)
