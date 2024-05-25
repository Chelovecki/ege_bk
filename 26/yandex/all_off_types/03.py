file = open('03 orig data.txt')

len_of_numbers = int(file.readline())

numbers = sorted([int(r) for r in file.readlines()], reverse=True)

best_present = [numbers[0]]
l = 0
for r in range(1, len(numbers)):
    a = numbers[l]
    b = numbers[r]
    if a - b >= 11:
        best_present.append(numbers[r])
        l = r
print(len(best_present), min(best_present))
