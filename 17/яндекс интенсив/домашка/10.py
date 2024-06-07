numbers = [int(r) for r in open('17 10.txt').readlines()]
c = m = 0

for idx in range(2, len(numbers)):
    a = numbers[idx - 2:idx + 1]
    if all([1000 <= r <= 9999 for r in a]):
        first = sum([int(symb) for symb in str(a[0])])
        second = sum([int(symb) for symb in str(a[1])])
        third = sum([int(symb) for symb in str(a[2])])
        this_obj = [first, second, third]
        if len(this_obj) == len(set(this_obj)):
            s = sum([int(num) for num in a])
            if str(s) == str(s)[::-1]:
                c += 1
                m = max(m, max([first, second, third]))
print(c, m)
