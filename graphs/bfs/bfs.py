from typing import List


def recursiveBFS(graph: List[List[int]], q: List[int], visited: List[bool], key: int):
    if not q:
        return "Not Found"

    # pop last node from queue and print it
    v = q.pop()
    if v == key:
        return "Found"

    # do for every neighbors of node v
    for u in graph[v]:
        if not visited[u]:
            # mark it visited and push it into queue
            visited[u] = True
            q.append(u)

    # recurse for other nodes
    recursiveBFS(graph, q, visited, key)


def iterativeBFS(graph: List[List[int]], s: int, visited: List[int], key: int):
    # create a queue needed for BFS
    q = []

    # mark source node as discovered
    visited[s] = True

    # push source node into the queue
    q.append(s)

    # while queue isn't empty
    while q:
        # pop last node from queue and print it
        v = q.pop()
        if v == key:
            return "Found"

        # for every neighboring node of v
        for u in graph[v]:
            if not visited[u]:
                # mark it visited and enqueue to queue
                visited[u] = True
                q.append(u)

    # If key hasn't been found
    return "Not Found"
