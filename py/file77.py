# 7. BFS (queue bilan)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v not in visited:
            print(v, end=" ")
            visited.add(v)
            queue.extend(graph[v])
            