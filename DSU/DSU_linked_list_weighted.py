class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.root = None

class HeadNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length


nodes = {}

def make_set(x):
    S = HeadNode()
    n = Node(x)
    n.root = S
    S.head = S.tail = n
    S.length = 1
    nodes[x] = n

def find_set(x: Node):
    return x.root

def link(rx: HeadNode, ry: HeadNode):
    ry.tail.next = rx.head
    ry.tail = rx.tail
    ry.length += rx.length

    curr = rx.head
    while curr:
        curr.root = ry
        curr = curr.next

def union(x: Node, y: Node):
    rx = find_set(x)
    ry = find_set(y)
    if rx is ry:
        return

    if len(rx) < len(ry):
        link(rx, ry)
    else:
        link(ry, rx)
