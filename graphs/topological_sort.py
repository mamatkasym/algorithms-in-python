"""
The topological sort algorithm takes a directed graph and returns an array of the nodes where each node appears
before all the nodes it points to
    - As a rule, cyclic graphs don't have valid topological orderings.
    - Topological order can be non-unique
"""
from collections import defaultdict, Counter, deque


def topological_sort(digraph: dict) -> list[int]:

    seen = defaultdict(lambda: False)
    degree = Counter()
    for v in digraph:
        for edge in digraph[v]:
            degree[edge] += 1

    result = []
    q = deque()
    for v in digraph:
        if degree[v] == 0:
            seen[v] = True
            q.append(v)

    while q:
        ve = q.popleft()
        result.append(ve)
        for edge in digraph.get(ve, {}):
            degree[edge] -= 1

            if not seen[edge] and degree[edge] == 0:
                seen[edge] = True
                q.append(edge)
    return result if len(result) >= len(digraph) else []


def test_topological_sort():
    digraph = {'A': {'C', 'D'}, 'B': {'C', 'E'}, 'C': {'D'}, 'E': {'A', 'C'}}
    print(topological_sort(digraph))

test_topological_sort()
