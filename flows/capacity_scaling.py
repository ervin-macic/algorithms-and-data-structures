from collections import defaultdict
from typing import List
from math import log2, floor
MAXN = 100
graph = [[] for _ in range(MAXN)]
c = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
f = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
r = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
seen = defaultdict(bool)
n = 0

def add_edge(i, j, cap):
    c[i][j] = cap
    graph[i].append(j)
    graph[j].append(i)
    r[i][j] = c[i][j]
    f[i][j] = 0 # unnecessary?

def add_flow(i, j, x):
    f[i][j] += x 
    f[j][i] -= x
    r[i][j] -= x 
    r[j][i] += x

def clear_flow():
    for i in range(n+1):
        for j in range(n+1):
            f[i][j] = 0
            r[i][j] = c[i][j]

def clear_seen():
    global seen 
    seen = defaultdict(bool)
    

def augment_path(path):
    bottleneck = min([r[u][v] for u,v in zip(path, path[1:])])
    for u,v in zip(path, path[1:]):
        add_flow(u, v, bottleneck)

def scaled_find_augmenting_path(s, t, delta) -> (List[int], bool):
    seen[s] = True 
    if s == t:
        return [s], True 
    else:
        for v in graph[s]:
            if not seen[v] and r[s][v] >= delta:
                path, reaching = scaled_find_augmenting_path(v, t, delta)
                if reaching:
                    path = [s] + path 
                    return path, True
    return [], False

def scaled_ford_fulkerson():
    C = max(max(row) for row in c)
    delta = 2 ** (floor(log2(C))) # largest power of 2 at most max capacity
    while delta >= 1: # run at most 1 + log(C) times
        while True: # at most O(m) iterations since each augment path increases f by at least delta and   
            clear_seen()
            path, reaching = scaled_find_augmenting_path(s, t, delta) # O(m) since DFS
            if not reaching:
                break
            augment_path(path)
        delta //= 2
    return f

# Colab large example
# s = 1
# t = 8
# edges = [(1, 2, 10), (1, 3, 5), (1, 4, 15), (2, 5, 9), (2, 6, 15), (2, 3, 4), (3, 6, 8), (3, 4, 4), (5, 8, 10), (5, 6, 15), (6, 8, 10), (6, 7, 15), (7, 3, 6), (7, 8, 10)]
# n = 8
# for (i, j, cap) in edges:
#     add_edge(i, j, cap)

# scaled_ford_fulkerson()
# for i in range(n+1):
#     for j in range(n+1):
#         if r[i][j] != 0:
#             print(f"({i,j} with residue: {r[i][j]}")


# Problem sheet example
s = 1
t = 4
edges = [(1,2,256), (1,3,255), (2,3,1), (2,4,255), (3,4,256)]
n = 4
for (i, j, cap) in edges:
    add_edge(i, j, cap)

scaled_ford_fulkerson()