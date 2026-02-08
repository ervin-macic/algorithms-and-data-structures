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


def edmonds_karp(s, t):
    while True:
        clear_seen_and_p()
        min_path, reaching = bfs_find_augmenting_path(s, t)
        if not reaching:
            break
        augment_path(min_path)
    min_cut = sum(f[s][v] for v in range(1, 9))
    return min_cut

n = 8
edges = [(1,2), (1,3), (1,5), (2,4), (4,3), (3,7), (5,7), (2,6), (5,6), (4,8), (6,8), (7,8)]
for (i, j) in edges:
    graph[i].append(j)
    graph[j].append(i)
    c[i][j] = 1
    c[j][i] = 1
    r[i][j] = 1
    r[j][i] = 1
    f[i][j] = 0
    f[j][i] = 0

s = 1
edge_connectivity = float("inf")
for t in range(2, n + 1):
    clear_flow()
    clear_seen_and_p()
    min_cut_val = edmonds_karp(s, t)
    edge_connectivity = min(edge_connectivity, min_cut_val)
print(f"Edge Connectivity: {edge_connectivity}")

