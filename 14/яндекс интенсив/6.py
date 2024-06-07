for x in '0123456789abcdefghi':
    n = int(f"98897{x}21",19)+  int(f'2{x}923',19)
    if n % 18 == 0:
        print(n//18)