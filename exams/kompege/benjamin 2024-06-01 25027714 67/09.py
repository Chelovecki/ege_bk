numbers = [list(map(int, r.split(','))) for r in open('09_9878.csv').readlines()]

s = 0

for n, line in enumerate(numbers, 1):
    repeating = [r for r in line if line.count(r) == 3]
    if len(repeating) == 3 and len([r for r in line if line.count(r) == 1]) == 4:
        mi = min(line)
        ma = max(line)
        if repeating[0] != mi and repeating[0] != ma:
            s += n

print(s)
