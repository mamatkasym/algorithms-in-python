from abc import ABC
from typing import Sequence, Hashable


class Node:
    """Node or vertex object implementation"""
    def __init__(self, val: Hashable):
        self.val = val


class Edge:
    __slots__ = ('start', 'end', 'weight')

    def __init__(self, start: Node, end: Node, weight: int = None):
        self.start = start
        self.end = end
        self.weight = weight

class Graph(ABC):
    nodes: list[Node]
    edges: list[Edge]

    def __init__(self, nodes: Sequence[Node]=None):
        if not nodes:
            self.nodes = []
        else:
            self.nodes = list(nodes)

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, edge: Edge):
        raise NotImplementedError


class DirectedGraph(Graph):
    def add_edge(self, edge: Edge):
        self.edges.append(edge)

class UndirectedGraph(Graph):
    def add_edge(self, edge: Edge):
        self.edges.append(edge)
        self.edges.append(Edge(start=edge.end, end=edge.start, weight=edge.weight))
