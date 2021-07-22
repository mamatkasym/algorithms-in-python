"""
You are given a directed or undirected weighted graph with n vertices and m edges.
The weights of all edges are non-negative. You are also given a starting vertex s.
This article discusses finding the lengths of the shortest paths from a starting vertex s to all other vertices,
and output the shortest paths themselves.
"""
from typing import List, Tuple


# An algorithm described by the Dutch computer scientist Edsger W. Dijkstra in 1959

INF = 10 ** 10


def dijkstra(n: int, s: int, e: List[List], distance: List[int], marked: List[int]):
    """
    Time complexity: O(n^2 + m)
    """
    distance[s] = 0
    pred = [-1] * n
    for i in range(n):
        v = - 1
        for j in range(n):
            if not marked[j] and (v == -1 or distance[j] < distance[i]):
                v = j
        if distance[v] == INF:
            break

        marked[v] = True
        for edge in e[v]:
            to = edge[0]
            weight = edge[1]
            if distance[v] + weight < distance[to]:
                distance[to] = distance[v] + weight
                pred[to] = v

    print(pred)


def test():

    n = int(input())
    m = int(input())

    edges = [[None] for _ in range(n)]
    distance = [INF] * n
    marked = [False] * n

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))
        edges[v].append((u, w))
    print(edges)


test()
