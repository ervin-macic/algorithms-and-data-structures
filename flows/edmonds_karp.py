from collections import defaultdict, deque
from typing import List
MAXN = 100
graph = [[] for _ in range(MAXN)]
d = [0 for _ in range(MAXN)] # distance from source
p = [0 for _ in range(MAXN)] # parent for path reconstruction
c = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
f = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
r = [[0 for _ in range(MAXN)] for _ in range(MAXN)]
seen = defaultdict(bool)
n = 0

def add_edge(i, j, cap):
    c[i][j] = cap
    graph[i].append(j)
    graph[j].append(i)
    r[i][j] = cap
    r[j][i] = 0
    f[i][j] = 0
    f[j][i] = 0

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

def clear_seen_and_p():
    global seen, p
    seen = defaultdict(bool)
    p = [0 for _ in range(MAXN)]

def augment_path(path):
    bottleneck = min([r[u][v] for u,v in zip(path, path[1:])])
    for u,v in zip(path, path[1:]):
        add_flow(u, v, bottleneck)

def bfs_find_augmenting_path(s, t) -> (List[int], bool):
    q = deque()
    q.append(s)
    seen[s] = True
    while q:
        u = q.popleft()
        if u == t: # first time reaching target
            min_path = [u]
            # go through u's parents to reconstruct path leading to t
            while u != s:
                u = p[u]
                min_path.append(u)
            min_path.reverse()
            return min_path, True 
        
        for v in graph[u]:
            if not seen[v] and r[u][v] > 0:
                q.append(v)
                seen[v] = True
                p[v] = u
    return [], False

def edmonds_karp():
    while True:
        clear_seen_and_p()
        min_path, reaching = bfs_find_augmenting_path(s, t)
        if not reaching:
            break
        augment_path(min_path)
    return f

s = 1
t = 8
edges = [(1, 2, 10), (1, 3, 5), (1, 4, 15), (2, 5, 9), (2, 6, 15), (2, 3, 4), (3, 6, 8), (3, 4, 4), (5, 8, 10), (5, 6, 15), (6, 8, 10), (6, 7, 15), (7, 3, 6), (7, 8, 10)]
n = 8
for (i, j, cap) in edges:
    add_edge(i, j, cap)

edmonds_karp()
for i in range(n+1):
    for j in range(n+1):
        if r[i][j] != 0:
            print(f"({i,j} with residue: {r[i][j]}")

