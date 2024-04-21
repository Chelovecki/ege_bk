def condition(n):
    divizors = [divizor for divizor in range(2, int(n//2) +1) if n%divizor!=0 and divizor%2==0]

    return len(set(divizors)) == 3


for r in range(101_000_000, 102_000_001):
    if condition(r):
        print(r)