"""
You have a graph G with V vertices and E edges. The graph is a weighted graph but the weights have a constraint
that they can only be 0 or 1. Write an efficient code to calculate shortest path from a given source.
"""

from collections import deque

# Number of vertices in queue
N = int(input())

# Number of edges in queue
M = int(input())

# Graph representation
G = [[] for i in range(N)]
for _ in range(M):
    # vertices u and v are connected by edge with weight w in [0, 1]
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

INF = N + 1

# At the beginning set all distance from source vertex to INF
D = [INF for _ in range(N)]

# Set distance to source vertex to 0
D[0] = 0

# Initialize deque with single element source
dq = deque([0])

while dq:
    u = dq.popleft()
    for edge in G[u]:
        v = edge[0]
        w = edge[1]
        # Main logic here
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            if w == 0:
                dq.appendleft(v)
            else:
                dq.append(v)

# print distances
for i in range(N):
    print(D[i], end=" ")
