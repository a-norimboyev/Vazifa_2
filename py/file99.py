# 9. Graf bog‘langanligini tekshirish
def is_connected(graph, start):
    visited = set()

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return len(visited) == len(graph)