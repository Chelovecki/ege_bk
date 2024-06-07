for x in '0123456789abcdefgh'.upper():
    n = int(f'ABCD{x}', 15) + int(f'123{x}4', 15)
    if n % 14 == 0:
        print(n // 14)
        break
