from typing import List, Optional
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, val:int, parent = None):
        self.val = val 
        self.p = parent 
        self.left = None 
        self.right = None 

class SplayTree:
    def __init__(self, lst:List[int] = None):
        self.root = None
        if lst:
            for v in lst:
                new_node = Node(v)
                self.insert(new_node)
    
    def empty(self) -> bool: return self.root is None

    def right_rotate(self, y: Node):
        x = y.left
        if x is None:
            return # cannot rotate

        # move x's right subtree to y's left
        y.left = x.right
        if x.right:
            x.right.p = y

        # link x to y's parent
        x.p = y.p
        if y.p is None:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x

        # put y on x's right
        x.right = y
        y.p = x


    def left_rotate(self, x: Node):
        y = x.right
        if y is None:
            return  # cannot rotate

        # move y's left subtree to x's right
        x.right = y.left
        if y.left:
            y.left.p = x

        # link y to x's parent
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        # put x on y's left
        y.left = x
        x.p = y

    
    def splay(self, x:Node) -> None:
        while x.p != None:
            y = x.p
            # x has parent but no grandparent (one away from root)
            if x.p.p is None:
                if y.right == x:
                    self.left_rotate(y)
                else:
                    self.right_rotate(y)
            else:
                z = x.p.p

                # zig zig left
                if z.left == y and y.left == x:
                    self.right_rotate(z)
                    self.right_rotate(y)

                # zig zig right
                elif z.right == y and y.right == x:
                    self.left_rotate(z)
                    self.left_rotate(y)

                # zig zag 
                elif z.left == y and y.right == x:
                    self.left_rotate(y)
                    self.right_rotate(z)

                # zag zig
                else:
                    self.right_rotate(y)
                    self.left_rotate(z)

                

    def search(self, v:int) -> Optional[Node]:
        x = self.root 
        while x is not None and x.val != v:
            if x.val > v:
                x = x.left 
            else:
                x = x.right
        return x
    
    def insert(self, z:Node) -> None:
        if self.empty():
            self.root = z
            return
        
        x = self.root
        y = x
        while x is not None:
            y = x
            if x.val > z.val:
                x = x.left 
            else:
                x = x.right
        z.p = y
        if y.val > z.val:
            y.left = z 
        else:
            y.right = z
    
    def _max_from_node(self, x:Node) -> Node:
        assert x is not None 
        y = x
        while x != None:
            y = x
            x = x.right
        return y
    
    def max(self) -> Optional[int]:
        if self.empty():
            return None 
        return self._max_from_node(self.root).val
    
    def _min_from_node(self, x:Node) -> Node:
        assert x is not None 
        y = x
        while x != None:
            y = x
            x = x.left
        return y
    
    def min(self) -> Optional[int]:
        if self.empty():
            return None 
        return self._min_from_node(self.root).val
    
    def successor(self, x:Node) -> Optional[Node]:
        if x.right:
            return self._min_from_node(x.right)
        else:
            while x != self.root:
                x = x.p
                if x.right:
                    return self._min_from_node(x.right)
        
    def predecessor(self, x:Node) -> Optional[Node]:
        if x.left:
            return self._max_from_node(x.left)
        else:
            while x != self.root:
                x = x.p
                if x.left:
                    return self._max_from_node(x.left)

    def visualize(self, figsize=(6, 6), node_size=2000):

        if self.root is None:
            print("Tree is empty")
            return

        G = nx.DiGraph()
        pos = {}

        # Build graph and positions simultaneously
        def dfs(node, x, y, dx):
            if node is None:
                return

            G.add_node(node, label=str(node.val))
            pos[node] = (x, y)

            if node.left:
                G.add_edge(node, node.left)
                dfs(node.left, x - dx, y - 1, dx / 2)

            if node.right:
                G.add_edge(node, node.right)
                dfs(node.right, x + dx, y - 1, dx / 2)

        dfs(self.root, x=0, y=0, dx=1)

        labels = nx.get_node_attributes(G, "label")

        plt.figure(figsize=figsize)
        nx.draw(
            G,
            pos,
            with_labels=False,
            node_size=node_size,
            node_color="lightblue",
            arrows=False,
            width=3
        )

        for node, (x, y) in pos.items():
            plt.text(
                x,
                y,
                labels[node],
                ha="center",
                va="center",
                fontsize=20,
                fontweight="bold"
            )

        plt.title("Binary Search Tree")
        plt.axis("off")
        plt.show()


    def _transplant(self, u: Node, v: Optional[Node]):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v

        if v is not None:
            v.p = u.p

    def delete(self, x: Node) -> None:
        if x.left is None:
            self._transplant(x, x.right)

        elif x.right is None:
            self._transplant(x, x.left)

        else:
            y = self._min_from_node(x.right)  # successor

            if y.p != x:
                self._transplant(y, y.right)
                y.right = x.right
                y.right.p = y

            self._transplant(x, y)
            y.left = x.left
            y.left.p = y


tree = SplayTree()
n10 = Node(10)
tree.insert(n10)
n1 = Node(1, n10)
n12 = Node(12, n10)
n8 = Node(8, n1)
n4 = Node(4, n8)
n2 = Node(2, n4)
n6 = Node(6, n4)
n5 = Node(5, n6)
n10.right = n12 
n10.left = n1
n1.right = n8 
n8.left = n4 
n4.left = n2 
n4.right = n6 
n6.left = n5
tree.visualize()
tree.splay(n2)
tree.visualize()