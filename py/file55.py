# 5. Graf (qo‘shnichilik ro‘yxati)
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for v in self.graph:
            print(v, "->", self.graph[v])