# say elements in sets are {1,2,...,n}

import networkx as nx
import matplotlib.pyplot as plt


def visualize():
    global parent
    G = nx.DiGraph()
    G.add_nodes_from(range(1, n+1))

    # funny bug happened here, child, parent was present so running visualize twice made parent become an int haha
    for c, p in enumerate(parent):
        if p != c:
            G.add_edge(c, p)

    pos = nx.nx_agraph.graphviz_layout(
           G,
           prog="dot",
           args="-Grankdir=BT"
        )

    plt.figure(figsize=(8, 3))
    nx.draw(
        G,
        pos,
        with_labels=True,
        arrows=True,
        node_size=1200,
        node_color="lightblue",
        font_size=20,
    )
    print("-------------------------------------------")
    plt.show()
    print("-------------------------------------------")

n = 16
parent = [0] * (n+1)
h = [0] * (n+1)

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
        if h[rx] > h[ry]:
            link(ry, rx)
        elif h[rx] < h[ry]:
            link(rx, ry)
        else:
            link(rx, ry)
            h[ry] += 1

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
# n = 8
# parent = [0] * (n+1)
# h = [0] * (n+1)

# for i in range(1, n+1):
#     make_set(i)
# union(1, 2)
# union(3, 4)
# union(5, 6)
# union(7, 8)

# union(1, 3)
# union(5, 7)

# print(find_set(3))
# print(find_set(1))
# print(h[2], h[1], h[4], h[3])
# print(h[5], h[6], h[8], h[7])


