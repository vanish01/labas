class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)

    def dfs(self, residual_graph, s, t, parent):
        visited = [False] * self.num_vertices
        stack = [s]
        visited[s] = True

        while stack:
            u = stack.pop()
            for v in range(self.num_vertices):
                if not visited[v] and residual_graph[u][v] > 0:
                    stack.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def max_flow(self, source, sink):
        residual_graph = [row[:] for row in self.graph]
        parent = [-1] * self.num_vertices
        max_flow = 0

        while self.dfs(residual_graph, source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, residual_graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                residual_graph[u][v] -= path_flow
                residual_graph[v][u] += path_flow
                v = parent[v]

        return max_flow

def test_ford_fulkerson():
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    ff = FordFulkerson(graph)
    assert ff.max_flow(0, 5) == 23, "Тест не пройден"
    print("Все тесты пройдены!")

test_ford_fulkerson()