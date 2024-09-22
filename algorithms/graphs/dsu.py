"""
https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/

"""
from typing import Sequence

from algorithms.graphs.ds import UndirectedGraph
from algorithms.graphs.ds import Node


class UnionFind(UndirectedGraph):
    components: int
    size: int
    rank: list[int]
    parent: dict

    def __init__(self, nodes: Sequence):
        super().__init__(nodes)
        self.size = len(nodes)
        self.parent = {v: v for v in nodes}
        self.rank = [1 for _ in range(self.size)]
        self.components = self.size

    def find(self, p: Node) -> int:
        """Find parent of node `p` and compress simultaneously"""
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def is_connected(self, p: Node, q: Node) -> bool:
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        """Naive way to connect two components"""
        _p = self.parent[p]
        _q = self.parent[q]
        self.parent[_p] = _q

    def quick_union(self, p: Node, q: Node) -> None:
        """Faster union"""
        _p = self.find(p)
        _q = self.find(q)
        if _p == _q:
            # Components are already connected
            return
        # Merge the components
        if self.rank[_p] < self.rank[_q]:
            self.parent[_p] = _q
            self.rank[_q] += self.rank[_p]
        else:
            self.parent[_q] = _p
            self.rank[_p] += self.rank[_q]

        self.components -= 1
