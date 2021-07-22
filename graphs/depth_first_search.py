"""
    Tress depth first search implementation in Python
"""
from typing import List


def dfs(root: int, visited: List[bool], edges: List[List[int]]):
    pass


def recursive_dfs(root: int, visited: List[bool], edges: List[List[int]]):
    visited[root] = True
    print(root, end=' ')
    for node in edges[root]:
        if not visited[node]:
            recursive_dfs(node, visited, edges)


def main():
    n = int(input())
    edges = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    recursive_dfs(2, visited, edges)


if __name__ == '__main__':
    main()
