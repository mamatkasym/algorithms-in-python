from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def root(self, i: int) -> int:
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        pid = self.parent[p]
        qid = self.parent[q]

        for i in range(len(self.parent)):
            if self.parent[i] == pid:
                self.parent[i] = qid

    def quick_union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.parent[i] = j
            self.size[j] += self.size[i]
        else:
            self.parent[j] = i
            self.size[i] += self.size[j]


def connected(p: int, q: int, parent: List[int]) -> bool:
    return parent[p] == parent[q]
