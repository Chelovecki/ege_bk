for x in '0123456789ABCDEFGHIJKLMNOPQRSTUV':
    n = int(f"72{x}",32) + int(f"1C{x}7",32) + int(x,32)**5
    aliases = int(x,32)
    if aliases!=0 and n % aliases == 0:
        print(x,n/aliases)