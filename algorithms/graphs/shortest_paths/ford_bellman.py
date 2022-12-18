"""
Suppose given a graph with n vertices and m edges and some vertex v. It is required to find shortest paths from v
to all all vertices. Unlike Dijkstra's algorithm, this works for graph with edges with negative weights.
This algorithm is proposed by to american scientists Richard Bellman and Lester Ford in 1956.
"""


class Edge:
    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost


def shortest_paths(n: int, edges: list[Edge], s: int) -> list[float]:
    """
    Returns list of shortest paths from source vertex s to all vertices.
    Algorithm works in O(m*n) time.
    """
    m = len(edges)
    INF = float('inf')
    # d[i] if the shortest cost to travel from s to i
    d = [INF] * n
    # p[i] is the parent of vertex on i on the shortest path to i
    p = [0] * n
    d[s] = 0

    for _ in range(n-1):
        some = 0
        for e in edges:
            if d[e.u] < INF:
                d[e.v] = min(d[e.v], d[e.u] + e.cost)
                p[e.v] = e.u
                some += 1

        if not some:
            break
    return d
