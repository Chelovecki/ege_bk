numbers = [int(r) for r in open('17 47221.txt').readlines()]

max_num_in_seq = max([r for r in numbers if str(r).endswith('3')])

c = m = 0
for idx in range(1, len(numbers), 2):
    first = numbers[idx - 1]
    second = numbers[idx]

    # только 1 кончается на 3
    c1 = sum([
        str(first).endswith('3'),
        str(second).endswith('3')
    ]) == 1

    c2 = first ** 2 + second ** 2 >= m ** 2
    if c2 and c1:
        c += 1
        m = max(m, first ** 2 + second ** 2)
print(c, m)
