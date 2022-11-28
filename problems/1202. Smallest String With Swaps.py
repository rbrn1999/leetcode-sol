# link: https://leetcode.com/problems/smallest-string-with-swaps/

from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]
        self.rank = [0] * size
        
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def union(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        if group1 == group2:
            return False
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
        
        return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)

        goups = defaultdict(list)
        for i in range(len(s)):
            goups[uf.find(i)].append(s[i])
        for comp_id in goups.keys():
            goups[comp_id].sort(reverse=True)

        res = []
        for i in range(len(s)):
            res.append(goups[uf.find(i)].pop())

        return ''.join(res)
    # too slow
    # from copy import deepcopy
    # def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
    #     result = list(s)
    #     sets = []
    #     for pair in pairs:
    #         toJoin = []
    #         cur = set(pair)
    #         for item in deepcopy(sets):
    #             if cur.intersection(item) != set():
    #                 toJoin.append(item)
    #                 sets.remove(item)
    #         for item in toJoin:
    #             cur = cur.union(item)
    #         sets.append(cur)
    #     inds = [sorted(list(x)) for x in sets]
    #     for ind in inds:
    #         temp = sorted([s[i] for i in ind])
    #         for i, v in enumerate(ind):
    #             result[v] = temp[i]        
    #     return ''.join(result)
