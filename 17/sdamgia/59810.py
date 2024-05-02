numbers = [int(r) for r in open('59810.txt')]
max_ends_24 = max([r for r in numbers if str(r).endswith('24')])
c =0
m = 10_000

for idx in range(2, len(numbers)):
    f,s,t = numbers[idx - 2:idx + 1]
    a = numbers[idx - 2:idx + 1]
    if len([r for r in a if len(str(abs(r))) == 3]) == 1:
        if sum(a)>max_ends_24:
            c+=1
            m = min(m,sum(a))
print(c,m)
