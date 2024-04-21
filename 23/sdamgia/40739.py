def funk(s, f):
    if s > f: return 0
    if s == f: return 1

    return funk(s + 1, f) + funk(s + 2, f) + funk(s * 3, f)


print(funk(1, 8) * funk(8, 15))