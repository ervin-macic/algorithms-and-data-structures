def make_set(x):
    parent[x] = x 
    h[x] = 0

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

# Assuming rx, ry roots
def link(rx, ry):
    parent[rx] = ry

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return 
    else:
        if h[rx] < h[ry]:
            link(rx, ry)
        elif h[rx] > h[ry]:
            link(ry, rx)
        else:
            link(rx, ry)
            h[ry] += 1

# Example usage

n = 16
parent = [0] * (n+1)
h = [0] * (n+1)

for i in range(1,17):
    make_set(i)

for i in range(1, 16, 2):
    union(i, i+1)

for i in range(1, 14, 4):
    union(i, i+2)

union(1, 5)
union(11, 13)
union(1, 10)
find_set(2)
find_set(9)
