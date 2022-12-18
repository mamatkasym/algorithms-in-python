"""
You are given a directed or undirected weighted graph with n vertices and m edges.
The weights of all edges are non-negative. You are also given a starting vertex s.
This article discusses finding the lengths of the shortest paths from a starting vertex s to all other vertices,
and output the shortest paths themselves.
Algorithm:
    1. From each of the unvisited vertices, choose the vertex with the smallest distance and visit it
    2. Update the distance for each neighboring vertex, of the visited vertex, whose current distance is greater
        than its sum and the weight of the edge between them
    3. Repeat steps 1 and 2 until all the vertices are visited.

# An algorithm described by the Dutch computer scientist Edsger W. Dijkstra in 1959
"""

from heapq import heappop, heappush


def shortest_paths(n: int, edges: list[list[float]], start: int) -> list[float]:
    """
    Shortest distance paths from start vertex to all vertices
    Time complexity is O(m * log(n)), where n is number of vertices in the graph.
    """
    # d[i] is distance from start vertex to vertex i
    dis = [float("inf")] * n

    heap = [(0.0, start)]
    dis[start] = 0

    while heap:
        d, u = heappop(heap)
        # detour
        if dis[u] < d:
            continue
        for v, w in edges[u]:
            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                heappush(heap, (dis[v], v))

    return dis
