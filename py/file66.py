# 6. DFS (2 xil)
def dfs_recursive(graph, v, visited=set()):
    if v not in visited:
        print(v, end=" ")
        visited.add(v)
        for neighbor in graph[v]:
            dfs_recursive(graph, neighbor, visited)
            