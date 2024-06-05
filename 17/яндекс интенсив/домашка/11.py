numbers = [int(r) for r in open('17 11.txt').readlines()]
first_cond = [(numbers[idx - 1], numbers[idx]) for idx in range(1, len(numbers)) if
              (str(numbers[idx - 1]).endswith('7') + str(numbers[idx]).endswith('7')) == 1]
first_cond_but_with_modules = [abs(r[0] - r[1]) for r in first_cond]
print(first_cond_but_with_modules)
c = m = 0

for idx in range(1, len(numbers)):
    a = numbers[idx - 1:idx + 1]
    if len([r for r in a if str(r).endswith('7')]) == 1:
        if any([(a[0] - a[1]) ** 2 > obj for obj in first_cond_but_with_modules]):
            c += 1
            m = max(m, sum(a))
print(c, m)

# todo я не хочу решать эту задачу
