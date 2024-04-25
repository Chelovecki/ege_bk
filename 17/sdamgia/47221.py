data = [int(r) for r in open('47221.txt').readlines()]
max_elem = max([r for r in data if str(r)[-1] == '3']) **2
print(max_elem)
c = m = 0
for idx in range(len(data) - 1):
    first = data[idx]
    second = data[idx + 1]

    if (str(first)[-1] == '3' and str(second)[-1] != '3') or (str(first)[-1] != '3' and str(second)[-1] == '3'):
        if first ** 2 + second ** 2 >= max_elem:
            c += 1
            max_elem = max(max_elem, first ** 2 + second ** 2)
print(c, max_elem)


f = [abs(int(i)) for i in open("47221.txt")]
max_element = max(f, key=lambda x: x if x % 10 == 3 else -10_000)**2
print(max_element == max_elem
      )
result = []
for i in range(len(f) - 1):
    c = 0
    if f[i] % 10 == 3:
        c += 1
    if f[i + 1] % 10 == 3:
        c += 1
    if c == 1 and f[i]**2 + f[i + 1]**2 >= max_element:
        result.append(f[i]**2 + f[i + 1]**2)
print(len(result), max(result))