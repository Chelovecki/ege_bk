numbers = [int(r) for r in open('17 7.txt').readlines()]
max_3h_zna4 = max([r for r in numbers if 100<= abs(r) <=999])
c=m=0

for idx in range(1,len(numbers)):
    a = numbers[idx-1:idx+1]
    if len([r for r in a if len(str(abs(r))) ==3]) == 1:
        if sum(a) <= max_3h_zna4:
            c+=1
            m=max(m,sum(a))


print(c,m)