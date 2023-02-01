# link: https://leetcode.com/problems/number-of-good-paths/

from collections import defaultdict, Counter
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda: 0)

    def find(self, node: int):
        p = self.parent.setdefault(node, node)
        if p != self.parent[p]:
            p = self.find(p)
        return p

    def union(self, node1: int, node2: int):
        parent1, parent2 = self.find(node1), self.find(node2)
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        valToNodes = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        for node in range(len(vals)):
            valToNodes[vals[node]].add(node)

        unionFind = UnionFind()
        goodPaths = 0

        for val in sorted(list(set(vals))):
            for node in valToNodes[val]:
                goodPaths += 1
                for neighbor in graph[node]:
                    if vals[neighbor] <= vals[node]:
                        graph[neighbor].remove(node)
                        unionFind.union(node, neighbor)
            sizes = Counter([unionFind.find(node) for node in valToNodes[val]]).values()
            for size in sizes:
                if size > 1: # Combination(size, 2)
                    goodPaths += size * (size-1) // 2

        return goodPaths

