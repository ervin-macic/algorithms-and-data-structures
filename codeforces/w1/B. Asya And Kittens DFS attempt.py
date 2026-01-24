import sys
from collections import deque
def main():
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        (a,b) = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    ans = []
    def dfs(source):
        nonlocal graph, visited, ans
        visited[source] = True
        stack = deque()
        stack.append(source)
        while stack:
            next_node = stack.pop()
            ans.append(next_node)
            for neighbour in graph[next_node]:
                if not visited[neighbour]:
                    stack.append(neighbour)
                    visited[neighbour] = True
    for i in range(1, n + 1):
        if len(graph[i]) == 1:
            dfs(i)
            break
    result = " ".join(map(str, ans))
    print(result)

if __name__ == "__main__":
    main()