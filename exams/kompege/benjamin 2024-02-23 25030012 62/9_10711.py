
numbers = [list(map(int, r.rstrip('\n').split(';'))) for r in open('9_10711.csv')]

for r in numbers:
    max_num_here = max(r)
    repeating = [r.count(num) for num in r]
    if repeating.count(1) == 3 and repeating.count(2) == 4 and r.count(max_num_here) == 1:
        print(r, sum(r))
        break
print(f"ответ сумма, то есть, {sum(r)}")