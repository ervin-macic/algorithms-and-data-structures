def visualize():
    print(R)

n = 16
R = [0] * (n+1)
Rinv = [[] for _ in range(n+1)]

def make_set(x):
    R[x] = x
    Rinv[x].append(x)

def find_set(x):
    return R[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return 
    else:
        if len(Rinv[rx]) > len(Rinv[ry]):
            for elem in Rinv[ry]:
                R[elem] = rx
                Rinv[rx].append(elem)
            Rinv[ry].clear()
        else:
            for elem in Rinv[rx]:
                R[elem] = ry 
                Rinv[ry].append(elem)
            Rinv[rx].clear()

for i in range(1,17):
    make_set(i)
visualize()

for i in range(1, 16, 2):
    union(i, i+1)
visualize()

for i in range(1, 14, 4):
    union(i, i+2)
visualize()

union(1, 5)
union(11, 13)
union(1, 10)
visualize()
find_set(2)
visualize()
find_set(9)
visualize()


