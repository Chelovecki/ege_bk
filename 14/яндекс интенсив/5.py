import string

for x in '0123456789abcde':
    n = int(f'9897{x}21', 15) + int(f"12{x}023", 15)
    if n % 14 == 0:
        print(n // 14)
        break
