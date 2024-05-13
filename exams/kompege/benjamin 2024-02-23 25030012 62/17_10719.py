numbers = [int(r) for r in open('17_10719.txt')]

counter_pairs = max_val_couple = 0
for idx in range(0, len(numbers) - 3):
    first = numbers[idx]
    second = numbers[idx + 3]
    f_s = str(first)
    s_s = str(second)
    if (f_s.endswith('13') and not s_s.endswith('13')) or (not f_s.endswith('13') and s_s.endswith('13')):
        counter_pairs += 1
        if first + second >= max_val_couple:
            max_val_couple = first + second
print(counter_pairs, max_val_couple)

# странно, конечно, что так мало вышло. но и значений у нас поменьше (так как каждый 3й)
