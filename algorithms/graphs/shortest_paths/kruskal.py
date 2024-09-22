from typing import Sequence

from algorithms.graphs.dsu import UnionFind
from algorithms.graphs.ds import Edge


class Kruskal(UnionFind):
    mst_weight: int = 0
    mst: list[Edge]

    def shortest_path(self):
        self.edges.sort(key=lambda edg: edg.weight)
        i, e = 0, 0

        while e < self.size - 1:  # iterate until number of edges equals to nodes number - 1
            edge = self.edges[i]
            u = self.find(edge.start)
            v = self.find(edge.end)
            if u != v:  # TODO: implement node __eq__() method
                e += 1
                self.mst_weight += edge.weight
                self.mst.append(edge)
                self.quick_union(edge.start, edge.end)


