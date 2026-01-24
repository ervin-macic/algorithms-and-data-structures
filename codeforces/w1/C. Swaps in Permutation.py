import sys
from collections import defaultdict
def main():
    input = sys.stdin.readline
    n, m = map(int, input().strip().split())
    s = list(map(int, input().strip().split()))
    
    parent = [0] * (n + 1)
    h = [0] * (n + 1)

    def make_set(x):
        parent[x] = x 
        h[x] = 0
    
    def find_set(x):
        if x != parent[x]:
            parent[x] = find_set(parent[x])
        return parent[x]
    
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

    # Example

    for k in range(1, n+1):
        make_set(k)
    
    for _ in range(m):
        (a,b) = map(int, input().strip().split())
        union(a, b)

    # Handle sorted positions and mutate original permutation
    positions = defaultdict(list)
    unique_roots = set()

    for x in range(1, n+1):
        rx = find_set(x)
        unique_roots.add(rx)
        positions[rx].append(x)
    
    for root in unique_roots:
        lst = []
        for pos in positions[root]: # a sorted list of positions
            # pos ranges over 1,4,7 for example
            lst.append(s[pos-1])

        lst.sort(reverse=True)
        idx = 0
        for pos in positions[root]:
            s[pos-1] = lst[idx]
            idx += 1
    print(" ".join(map(str,s)))
        
        
    
if __name__ == "__main__":
    main()
# Input:
# 9 6
# 1 2 3 4 5 6 7 8 9
# 1 4
# 4 7
# 2 5
# 5 8
# 3 6
# 6 9
