# метод кабанова бы дай бог вспомнить

def from_150_to_10(n: str):
    n = n.split()[::-1]
    res = 0
    for n, r in enumerate(n):
        res += int(r) * 150 ** n
    return res


for x in range(1, 150):
    first = from_150_to_10(f"5 1 {x} 2 9")
    second = from_150_to_10(f"{x} 0 2 3")
    if (first + second) % 149 == 0:
        print((first + second) // 149)

# как же обалденно, что я вспомнил правила перевода в 10сс, и что там индексация начинается с нуля (такую задачу уже решал, она в репо)
