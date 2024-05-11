from fnmatch import fnmatch

for r in range(2024, 10**10, 2024):
    if fnmatch(str(r), '112?57*4'):
        if sum([int(b) for b in str(r)])%2==1:
            print(r,r//2024)