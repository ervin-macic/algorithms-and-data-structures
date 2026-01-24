# say elements in sets are {1,2,...,n}
import copy
import networkx as nx
import matplotlib.pyplot as plt

from matplotlib import animation

def make_gif(filename="dsu.gif", fps=2):
    fig, ax = plt.subplots(figsize=(8, 3))

    fig.subplots_adjust(top=0.78)

    def update(i):
        frame = frames[i]
        draw_parent_state(frame, ax)

        op = frame["op"]
        node = frame["node"]

        if op is None:
            title = f"Step {i}"
        else:
            title = f"Step {i}: {op}({node})"

        fig.suptitle(title, fontsize=14)

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=len(frames),
        interval=1000 // fps
    )

    anim.save(filename, writer="pillow")
    plt.close()


frames = []

def record_frame(op=None, node=None):
    frames.append({
        "parent": copy.deepcopy(parent),
        "op": op,
        "node": node
    })


def draw_parent_state(frame, ax):
    parent_state = frame["parent"]
    active = frame["node"]

    G = nx.DiGraph()
    G.add_nodes_from(range(1, n+1))

    for c, p in enumerate(parent_state):
        if c != 0 and p != c:
            G.add_edge(c, p)

    pos = nx.nx_agraph.graphviz_layout(
        G, prog="dot", args="-Grankdir=BT"
    )

    ax.clear()

    node_colors = [
        "orange" if v == active else "lightblue"
        for v in G.nodes()
    ]

    nx.draw(
        G,
        pos,
        with_labels=True,
        arrows=True,
        node_size=1200,
        node_color=node_colors,
        font_size=20,
        ax=ax
    )



n = 16
parent = [0] * (n+1)
h = [0] * (n+1)

def make_set(x):
    parent[x] = x
    h[x] = 0
    record_frame(op="make_set", node=x)


def find_set(x):
    if x != parent[x]:
        root = find_set(parent[x])
        parent[x] = root
        record_frame(op="path_compress", node=x)
    return parent[x]


# Assuming rx, ry roots
def link(rx, ry):
    parent[rx] = ry
    record_frame(op="link", node=[rx, ry])

def union(x, y):
    record_frame(op="union_start", node=[x,y])
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return
    if h[rx] > h[ry]:
        link(ry, rx)
    elif h[rx] < h[ry]:
        link(rx, ry)
    else:
        link(rx, ry)
        h[ry] += 1


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

make_gif("dsu_path_compression_v2.gif", fps=1.5)