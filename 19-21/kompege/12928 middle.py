from functools import lru_cache


def m(h):
    return h + 1, h * 2
@lru_cache
def g(h):
    if h >= 21: return "w"

    if any(g(r) == 'w' for r in m(h)): return "p1"
    if all(g(r) == 'p1' for r in m(h)): return "v1"

    if any(g(r) == 'v1' for r in m(h)): return "p2"
    if all(g(r) == 'p1' or g(r) == "p2" for r in m(h)): return "v2"

    if any(g(r) == 'v2' for r in m(h)): return "p3"

for stone in range(1,21):
    print(stone, g(stone))

print("---------")
print("19)", min([r for r in range(1,21) if g(r) == "p2"]))
print("20)", min([r for r in range(1,21) if g(r) == "v2"]))
print("21)", [r for r in range(1,21) if g(r) == "p3"][:2])
