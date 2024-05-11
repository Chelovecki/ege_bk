for r in range(1, 37):
    try:
        if int('TH', r) + int('NQ', r) + int('U', r) == int('1L7', r):
            print(r)
    except ValueError:
        pass
