for n in range(100):
    s = "!" + 15*'0' + n*'1' + 19*'2'

    while '!1' in s or '!2' in s or '!0' in s:
        if '!1' in s:
            s = s.replace('!1', '2!', 1)

        if '!2' in s:
            s = s.replace('!2', '30!', 1)

        if '!0' in s:
            s = s.replace('!0', '1!', 1)
    s = s.replace('0', '5', 1)
    s = s.replace('!', "")
    s_like_int = sum(map(int, list(s)))
    res = [(x**2) + (y**2) == s_like_int for x in range(1, 30) for y in range(1,30)]
    if any(res):
        print(n)
        break