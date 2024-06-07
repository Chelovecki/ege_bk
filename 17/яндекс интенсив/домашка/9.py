numbers = [int(r) for r in open('17 9.txt').readlines()]
min_end_8 = min([r for r in numbers if 100 <= abs(r) <= 999 and str(r).endswith('8')])
c=m=0

for idx in range(2,len(numbers)):
    a = numbers[idx-2:idx+1]
    if len([r for r in a if r ** 2 > min_end_8 ** 2])==2:
        if len([r for r in a if 100<=abs(r)<=999]):
            c+=1
            m=max(m,sum(a))


print(c,m)