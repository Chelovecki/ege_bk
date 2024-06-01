def to_13(x):
    if x % 13 == 12:
        return True
    return False


numbers = [int(r) for r in open('17_9872.txt').readlines()]
max_ends_12_in_13cc = max(r for r in numbers if to_13(r))

m = c = 0

for id in range(2, len(numbers)):
    a = numbers[id - 2:id + 1]

    if len([r for r in a if 100 <= abs(r) <= 999]) == 2:
        if sum(a) < max_ends_12_in_13cc:
            c += 1
            m = max(m, a[0] * a[1] * a[2])
print(c, m)
