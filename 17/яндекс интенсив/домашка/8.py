numbers = [int(r) for r in open('17 8.txt').readlines()]
max_end_17 = max([r for r in numbers if str(r).endswith('17')])
c=0
m=100_000

for idx in range(2,len(numbers)):
    a = numbers[idx-2:idx+1]
    if len([r for r in a if str(r).endswith('17')]) >= 1:
        if sum([abs(r) for r in a]) <= max_end_17:
            c+=1
            m=min(m,sum(a))


print(c,m)